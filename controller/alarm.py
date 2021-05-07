from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import and_
from model.model import Device, Pond, add, delete, commit, User, Sensor_threshold, Alarm

alarm = Blueprint('alarm', __name__)


@alarm.route('/alarm')
def go_alarm():
    alarms = Alarm.query.all()
    return render_template('alarm.html', alarms=alarms)


@alarm.route('/save_alarm', methods=['POST'])
def save_alarm():
    page = 1
    # 接收页码
    if request.values.get('page'):
        page = int(request.values.get('page'))
    id = request.form.get('id')
    col_time = request.form.get('col_time')
    col_value = request.form.get('col_value')
    sensor_type = request.form.get('sensor_type')
    area = request.form.get('area')
    pond_name = request.form.get('pond_name')
    alarm_type = request.form.get('alarm_type')

    if id:
        Alarm.query.filter(Alarm.id == id).update({'col_time': col_time, 'col_value': col_value, 'sensor_type': sensor_type, 'area': area, 'pond_name': pond_name, 'alarm_type': alarm_type})
        commit()
    else:
        alarm = Alarm(col_time, col_value, sensor_type, area, pond_name, alarm_type)
        add(alarm)
    alarms = Alarm.query.paginate(page=page, per_page=10)
    return toJson(alarms)


@alarm.route('/select_alarm', methods=['GET', 'POST'])
def select_alarm():
    page = 1
    # 接收页码
    if request.values.get('page'):
        page = int(request.values.get('page'))
    col_time = request.values.get('col_time')
    col_value = request.values.get('col_value')
    sensor_type = request.values.get('sensor_type')
    area = request.values.get('area')
    pond_name = request.values.get('pond_name')
    alarm_type = request.values.get('alarm_type')
    query = Alarm.query

    if col_time:
        query = query.filter(and_(Alarm.col_time.like('%{col_time}%'.format(col_time=col_time))))
    if col_value:
        query = query.filter(and_(Alarm.col_value.like('%{col_value}%'.format(col_value=col_value))))
    if sensor_type:
        query = query.filter(and_(Alarm.sensor_type.like('%{sensor_type}%'.format(sensor_type=sensor_type))))
    if area:
        query = query.filter(and_(Alarm.area.like('%{area}%'.format(area=area))))
    if pond_name:
        query = query.filter(and_(Alarm.pond_name.like('%{pond_name}%'.format(pond_name=pond_name))))
    if alarm_type:
        query = query.filter(and_(Alarm.alarm_type.like('%{alarm_type}%'.format(alarm_type=alarm_type))))
    # 重新查表
    alarms = query.paginate(page=page, per_page=10)
    return toJson(alarms)


@alarm.route('/delete_alarm', methods=['POST'])
def delete_alarm():
    page = 1
    # 接收页码
    if request.values.get('page'):
        page = int(request.values.get('page'))
    id = request.values.get('id')
    obj = Alarm.query.filter(Alarm.id == id).first()
    delete(obj)
    alarms = Alarm.query.paginate(page=page, per_page=10)
    return toJson(alarms)


def toJson(alarms):
    res = []
    for alarm in alarms.items:
        res.append(alarm.serialize())
    ret = {'items': res, 'page': alarms.page, 'total': alarms.total}
    return jsonify(ret)
