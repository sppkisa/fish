# 数据库模型
from flask_login import UserMixin, login_manager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

from main import app

# 现在直接在这个model文件里，创建各种模型，后期再分为各个model.py，否则下面这个app的配置都得写一遍，反正现在模型比较少，影响不大
# 数据库连接配置信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/fishpond'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 通用数据库操作,controller层调用的
def add(obj):
    db.session.add(obj)
    db.session.commit()


def delete(obj):
    db.session.delete(obj)
    db.session.commit()


def commit():
    db.session.commit()


# 创建Pond即水塘模型
class Pond(db.Model):
    def __init__(self, name, type, area):
        self.pond_name = name
        self.fish_type = type
        self.area_name = area

    # 定义表名
    __tablename__ = 'pond'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pond_name = db.Column(db.String(50))
    fish_type = db.Column(db.String(50))
    area_name = db.Column(db.String(50))

    def serialize(self):
        return {"id": self.id,
                "pond_name": self.pond_name,
                "fish_type": self.fish_type,
                "area_name": self.area_name
                }


# 创建设备device模型
class Device(db.Model):
    # 定义表名
    __tablename__ = 'device'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    type = db.Column(db.String(50), unique=True)
    state = db.Column(db.Boolean)


# 创建用户User模型
class User(db.Model, UserMixin):
    def __init__(self, name, password, type, phone, wechat):
        self.user_name = name
        self.user_password = password
        self.user_type = type
        self.user_phone = phone
        self.user_wechat = wechat

    # 定义表名
    __tablename__ = 'user'
    # 定义字段
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(50), unique=True)
    user_password = db.Column(db.String(255))  # hash密文
    user_type = db.Column(db.Integer)
    user_phone = db.Column(db.String(50))
    user_wechat = db.Column(db.String(50))

    def serialize1(self):
        return {
            "user_id": self.user_id,
            "user_name": self.user_name,
            "user_password": self.user_password,
            "user_type": self.user_type,
            "user_phone": self.user_phone,
            "user_wechat": self.user_wechat
        }

    def verify_password(self, password):
        """密码hash验证"""
        return check_password_hash(self.user_password, password)

    def get_id(self):
        """获取用户ID"""
        return self.user_id

    'pbkdf2:sha256:150000$zjAtWRkd$09214aadea84da0cc0f1569d2f63b3480e78d331f39ff80e94d1115e6d646d90'
    'pbkdf2:sha256:150000$nJ5AYDJL$f977916ea3eb746405d5dee8452f9e173b6da171cd1f73847e0461ecddbf410d'

    @staticmethod
    def get(user_name):
        """根据用户ID获取用户实体，为 login_user 方法提供支持"""
        if not user_name:
            return None
        user = User.query.filter(User.user_name == user_name).first()

        if user:
            return user
        return None

    @staticmethod
    def get_by_id(user_id):
        """根据用户ID获取用户实体，为 login_user 方法提供支持"""
        if not user_id:
            return None
        user = User.query.get(user_id)

        if user:
            return user
        return None

class Sensor_threshold(db.Model):
    def __init__(self, type, max1, min1, pond_name, area_name, max2, min2):
        self.type = type
        self.max1 = max1
        self.min1 = min1
        self.pond_name = pond_name
        self.area_name = area_name
        self.max2 = max2
        self.min2 = min2

    # 定义表名
    __tablename__ = 'sensor_threshold'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.Integer)
    max1 = db.Column(db.Float)
    min1 = db.Column(db.Float)
    pond_name = db.Column(db.String(50))
    area_name = db.Column(db.String(50))
    max2 = db.Column(db.Float)
    min2 = db.Column(db.Float)

    def serialize1(self):
        return {
            "id": self.id,
            "type": self.type,
            "max1": self.max1,
            "min1": self.min1,
            "pond_name": self.pond_name,
            "area_name": self.area_name,
            "max2": self.max2,
            "min2": self.min2
        }


class Alarm(db.Model):
    def __init__(self, col_time, col_value, sensor_type, area, pond_name, alarm_type):
        self.col_time = col_time
        self.col_value = col_value
        self.sensor_type = sensor_type
        self.area = area
        self.pond_name = pond_name
        self.alarm_type = alarm_type

    # 定义表名
    __tablename__ = 'alarm'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    col_time = db.Column(db.TIMESTAMP)
    col_value = db.Column(db.String(50))
    sensor_type = db.Column(db.Integer)
    area = db.Column(db.String(50))
    pond_name = db.Column(db.String(50))
    alarm_type = db.Column(db.String(50))

    def serialize(self):
        return {
            "id": self.id,
            "col_time": self.col_time,
            "col_value": self.col_value,
            "sensor_type": self.sensor_type,
            "area": self.area,
            "pond_name": self.pond_name,
            "alarm_type": self.alarm_type
        }
