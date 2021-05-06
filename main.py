from flask import Flask

app = Flask(__name__)

from controller.pond import pond
from controller.common import common
from controller.device import device
from controller.dashboard import dashboard
from controller.user import user
from controller.sensor_threshold import sensor_threshold
from controller.alarm import alarm

# 注册路由表
app.register_blueprint(common)
app.register_blueprint(pond)
app.register_blueprint(device)
app.register_blueprint(dashboard)
app.register_blueprint(user)
app.register_blueprint(sensor_threshold)
app.register_blueprint(alarm)
# jinja2模版渲染热更新设置
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['JSON_AS_ASCII'] = False
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

