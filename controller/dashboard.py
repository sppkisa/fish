import threading

from flask import Blueprint, render_template, jsonify, redirect, url_for, request
from flask_login import current_user
from kafka import KafkaConsumer

import pandas as pd
from pyflink.table import *

from pyflink.table.udf import udf
import numpy as np
import time

from sklearn.ensemble import IsolationForest

env_settings = EnvironmentSettings.new_instance().in_streaming_mode().use_blink_planner().build()
t_env = StreamTableEnvironment.create(environment_settings=env_settings)

t_env.get_config().get_configuration().set_string(
    "parallelism.default", "1")

t_env.get_config().get_configuration().set_boolean("python.fn-execution.memory.managed", True)
t_env.get_config().get_configuration().set_string("pipeline.jars",
                                                  "file:\\D:\\PPPCUT\\flink-connector-kafka_2.12-1.12.0.jar;file:\\D:\\PPPCUT\\flink-csv-1.12.0.jar;file:\\D:\\Repo\\org\\apache\\kafka\\kafka-clients\\1.0.0\\kafka-clients-1.0.0.jar")

train_data_path = "C:\\Users\\sankoo\\Desktop\\lunwen\\heihe_lxyc_20_10.csv"
source_data_path = "C:\\Users\\sankoo\\Desktop\\lunwen\\heihe_lxyc_20_10.csv"
result_data_path = "D:\\PPPCUT\\color.csv"

X_train = pd.read_csv(train_data_path,
                      names=['id', 'rowtime', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'label'], header=None)

X = np.array(pd.DataFrame(X_train, columns=['d1', 'd2', 'd3', 'd4', 'd5', 'd6']))
X = X[:24000, :]
start_time = time.time()

# IF = IsolationForest(n_estimators=100, max_samples=256)
#
# IF.fit(X)


# @udf(result_type=DataTypes.FLOAT())
# def predict(d1, d2, d3, d4, d5, d6,
#             ):
#     return IF.predict([d1, d2, d3, d4, d5, d6,
#                        ])


last = []
dashboard = Blueprint('dashboard', __name__)


@dashboard.before_request
def before_request():
    if current_user.is_authenticated is False:
        return redirect(url_for('common.login'))


@dashboard.route('/dashboard')
def go_dashboard():
    return render_template('dashboard.html')


# kafka接收数据的线程
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程： " + self.name)
        consumer = KafkaConsumer('water',
                                 bootstrap_servers=['121.196.54.227:9092'])
        print("????")
        for message in consumer:
            # message.value的字节形式：['b\'1','2018-01-01 00:00:00','6.93','9.03',....,'0\'']
            curr = {'name': str(message.value).split(',')[1],
                    'value': str(message.value).split(',')}
            last.append(curr)


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)

# 开启新线程
thread1.start()


@dashboard.route('/redraw', methods=['post'])
def getData():
    sensor_index = int(request.values.get('sensor'))
    threadLock = threading.Lock()
    global last
    ret = last
    # 获取锁，用于线程同步
    threadLock.acquire()
    last = []
    # 释放锁
    threadLock.release()
    # 检测ret，检测结果插表
    # [2]温度，[11]ph
    for v in ret:
        tem = v['value']
        print('sensor_index：'+str(sensor_index) + 'value:  ' + str(tem[sensor_index]))
        v['value'] = tem[sensor_index]
    return jsonify(ret)
