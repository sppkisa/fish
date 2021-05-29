from flask import Flask, redirect, url_for
from flask_login import LoginManager, login_required, current_user

app = Flask(__name__)

from controller.pond import pond
from controller.common import common
from controller.device import device
from controller.dashboard import dashboard
from controller.user import user
from controller.sensor_threshold import sensor_threshold
from controller.alarm import alarm
from controller.calendar import calendar
from controller.map_show import map_show

# 注册路由表
app.register_blueprint(common)
app.register_blueprint(pond)
app.register_blueprint(device)
app.register_blueprint(dashboard)
app.register_blueprint(user)
app.register_blueprint(sensor_threshold)
app.register_blueprint(alarm)
app.register_blueprint(calendar)
app.register_blueprint(map_show)
# jinja2模版渲染热更新设置
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['JSON_AS_ASCII'] = False

# 登陆安全设置
login_manager = LoginManager()  # 实例化登录管理对象
login_manager.init_app(app)  # 初始化应用
login_manager.login_view = 'common.login'  # 设置用户登录视图函数 endpoint
app.secret_key = 'abc'  # 设置表单交互密钥

from model.model import User


@login_manager.user_loader  # 定义获取登录用户的方法
def load_user(user_name):
    return User.get_by_id(user_name)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
