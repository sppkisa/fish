from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import and_
from model.model import Device, Pond, add, delete, commit, User, Sensor_threshold

sensor_threshold = Blueprint('sensor_threshold', __name__)


@sensor_threshold.route('/sensor_threshold')
def go_sensor_threshold():
    sensor_thresholds = Sensor_threshold.query.all()
    return render_template('sensor_threshold.html', sensor_thresholds=sensor_thresholds)


@sensor_threshold.route('/save_sensor_threshold', methods=['POST'])
def save_sensor_threshold():
    page = 1
    # 接收页码
    if request.values.get('page'):
        page = int(request.values.get('page'))
    id = request.form.get('id')
    type = request.form.get('type')
    max1 = request.form.get('max1')
    min1 = request.form.get('min1')
    pond_name = request.form.get('pond_name')
    area_name = request.form.get('area_name')
    max2 = request.form.get('max2')
    min2 = request.form.get('min2')

    if id:
        Sensor_threshold.query.filter(Sensor_threshold.id == id).update({'type': type, 'max1': max1, 'min1': min1, 'pond_name': pond_name, 'area_name': area_name, 'max2': max2, 'min2': min2})
        commit()
    else:
        sensor_threshold = Sensor_threshold(type, max1, min1, pond_name, area_name, max2, min2)
        add(sensor_threshold)
    sensor_thresholds = Sensor_threshold.query.paginate(page=page, per_page=10)
    return toJson(sensor_thresholds)


@sensor_threshold.route('/select_sensor_threshold', methods=['GET', 'POST'])
def select_sensor_threshold():
    page = 1
    # 接收页码
    if request.values.get('page'):
        page = int(request.values.get('page'))
    type = request.values.get('type')
    max1 = request.values.get('max1')
    min1 = request.values.get('min1')
    pond_name = request.values.get('pond_name')
    area_name = request.values.get('area_name')
    max2 = request.values.get('max2')
    min2 = request.values.get('min2')
    query = Sensor_threshold.query

    if type:
        query = query.filter(and_(Sensor_threshold.type.like('%{type}%'.format(type=type))))
    if max1:
        query = query.filter(and_(Sensor_threshold.max1.like('%{max1}%'.format(max1=max1))))
    if min1:
        query = query.filter(and_(Sensor_threshold.min1.like('%{min1}%'.format(min1=min1))))
    if pond_name:
        query = query.filter(and_(Sensor_threshold.pond_name.like('%{pond_name}%'.format(pond_name=pond_name))))
    if area_name:
        query = query.filter(and_(Sensor_threshold.area_name.like('%{area_name}%'.format(area_name=area_name))))
    if max2:
        query = query.filter(and_(Sensor_threshold.max2.like('%{max2}%'.format(max2=max2))))
    if min2:
        query = query.filter(and_(Sensor_threshold.min2.like('%{min2}%'.format(min2=min2))))
    sensor_thresholds = query.paginate(page=page, per_page=10)
    return toJson(sensor_thresholds)


@sensor_threshold.route('/delete_sensor_threshold', methods=['POST'])
def delete_sensor_threshold():
    page = 1
    # 接收页码
    if request.values.get('page'):
        page = int(request.values.get('page'))
    id = request.values.get('id')
    obj = Sensor_threshold.query.filter(Sensor_threshold.id == id).first()
    delete(obj)
    sensor_thresholds = Sensor_threshold.query.paginate(page=page, per_page=10)
    return toJson(sensor_thresholds)


def toJson(sensor_thresholds):
    res = []
    for sensor_threshold in sensor_thresholds.items:
        res.append(sensor_threshold.serialize1())
    ret = {'items': res, 'page': sensor_thresholds.page, 'total': sensor_thresholds.total}
    return jsonify(ret)
