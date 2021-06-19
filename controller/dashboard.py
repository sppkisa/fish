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

# env_settings = EnvironmentSettings.new_instance().in_streaming_mode().use_blink_planner().build()
# t_env = StreamTableEnvironment.create(environment_settings=env_settings)
#
# t_env.get_config().get_configuration().set_string(
#     "parallelism.default", "1")
#
# t_env.get_config().get_configuration().set_boolean("python.fn-execution.memory.managed", True)
# # flink的python环境 运行时调用java代码需要导入jar包
# t_env.get_config().get_configuration().set_string("pipeline.jars",
#                                                   # "file:\\D:\\PPPCUT\\flink-connector-kafka_2.12-1.12.0.jar;file:\\D:\\PPPCUT\\flink-csv-1.12.0.jar;file:\\D:\\Repo\\org\\apache\\kafka\\kafka-clients\\1.0.0\\kafka-clients-1.0.0.jar")
#                                                   "file:../files/flink-connector-kafka_2.12-1.12.0.jar;file:../files/flink-csv-1.12.0.jar;file:../files/kafka-clients-1.0.0.jar")
#
# # train_data_path = "C:\\Users\\sankoo\\Desktop\\lunwen\\heihe_lxyc_20_10.csv"
# # source_data_path = "C:\\Users\\sankoo\\Desktop\\lunwen\\heihe_lxyc_20_10.csv"
# train_data_path = "files/heihe_lxyc_20_10.csv"
# source_data_path = "files/heihe_lxyc_20_10.csv"
# # 这现在用不到 只创建这个目录 具体生成的文件名flink会自定义
# result_data_path = "D:\\PPPCUT\\color.csv"
#
# X_train = pd.read_csv(train_data_path,
#                       names=['id', 'rowtime', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'label'], header=None)
#
# X = np.array(pd.DataFrame(X_train, columns=['d1', 'd2', 'd3', 'd4', 'd5', 'd6']))
# X = X[:24000, :]
# start_time = time.time()

# IF = IsolationForest(n_estimators=100, max_samples=256)
#
# IF.fit(X)


# @udf(result_type=DataTypes.FLOAT())
# def predict(d1, d2, d3, d4, d5, d6,
#             ):
#     return IF.predict([d1, d2, d3, d4, d5, d6,
#                        ])


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
        self.last = []
        self.min_60 = 10000
        self.max_60 = -10000

    def run(self):
        print("开启线程： " + self.name)
        consumer = KafkaConsumer('water',
                                 bootstrap_servers=['121.196.54.227:9092'])
        for message in consumer:
            # message.value的字节形式：['b\'1','2018-01-01 00:00:00','6.93','9.03',....,'0\'']
            curr = {'name': str(message.value).split(',')[1],
                    'value': str(message.value).split(','),
                    }

            thread1.last.append(curr)


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)

# 开启新线程
thread1.start()


@dashboard.route('/redraw', methods=['post'])
def getData():
    # stat_index = int(request.values.get('stat'))
    sensor_index = int(request.values.get('sensor'))
    gap = int(request.values.get('gap'))
    threadLock = threading.Lock()
    ret = thread1.last
    # 获取锁，用于线程同步
    threadLock.acquire()
    thread1.last = []
    # 释放锁
    threadLock.release()

    # 检测ret，检测结果插表

    # stations = [3, 7, 11, 15, 19, 22]
    # [2]温度，[11]ph

    my_sum = 0
    avg = 0
    for v in ret:
        tem = v['value']
        # print('sensor_index：' + str(sensor_index) + 'value:  ' + str(tem[sensor_index]))
        # 应更换站点，接收来自不同站点（kafka topic）的数据 此处简略
        # 获取各个时间段的聚合结果 将来用flink任务可以很方便地统计，此处先粗略统计下
        # 先求出时间段差，除以间隔即为记录个数，

        if float(tem[sensor_index]) > thread1.max_60:
            thread1.max_60 = float(tem[sensor_index])
        if float(tem[sensor_index]) < thread1.min_60:
            thread1.min_60 = float(tem[sensor_index])
        my_sum += float(tem[sensor_index])
        # 总和除以记录个数即为结果
        v['value'] = tem[sensor_index]
    if len(ret) != 0:
        avg = my_sum / len(ret)
    res = {'min': thread1.min_60, 'max': thread1.max_60, 'avg': '%.3f' % avg, 'ret': ret}
    return jsonify(res)
