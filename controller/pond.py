from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import and_

from model.model import Device, Pond, add, delete, commit

pond = Blueprint('pond', __name__)


@pond.route('/pond')
def go_pond():
    ponds = Pond.query.all()
    return render_template('pond.html', ponds=ponds)


@pond.route('/save_pond', methods=['POST'])
def save_pond():
    page = 1
    # 接收页码
    if request.values.get('page'):
        page = int(request.values.get('page'))
    id = request.form.get('id')
    name = request.form.get('name')
    type = request.form.get('type')
    area = request.form.get('area')
    # 有两种情况 带id的是修改，不带id的是添加
    if id:
        Pond.query.filter(Pond.id == id).update({'pond_name': name, 'area_name': area, 'fish_type': type})
        commit()
    else:
        pond = Pond(name, type, area)
        add(pond)
        # 如果是修改 则不用跳转至第一页 如果是添加 则跳转至第一页
    ponds = Pond.query.paginate(page=page, per_page=10)
    return toJson(ponds)


@pond.route('/select_pond', methods=['GET', 'POST'])
def select_pond():
    page = 1
    # 接收页码
    if request.values.get('page'):
        page = int(request.values.get('page'))
    # 接收条件
    name = request.values.get('name')
    type = request.values.get('type')
    area = request.values.get('area')
    query = Pond.query
    # 条件封装
    if name:
        query = query.filter(and_(Pond.pond_name.like('%{name}%'.format(name=name))))
    if type:
        query = query.filter(and_(Pond.fish_type.like('%{type}%'.format(type=type))))
    if area:
        query = query.filter(and_(Pond.area_name.like('%{area}%'.format(area=area))))
    # 重新查表分页
    ponds = query.paginate(page=page, per_page=10)
    return toJson(ponds)


@pond.route('/delete_pond', methods=['POST'])
def delete_pond():
    page = 1
    # 接收页码
    if request.values.get('page'):
        page = int(request.values.get('page'))
    pond_id = request.values.get('id')
    obj = Pond.query.filter(Pond.id == pond_id).first()
    delete(obj)
    ponds = Pond.query.paginate(page=page, per_page=10)
    return toJson(ponds)


def toJson(ponds):
    res = []
    for pond in ponds.items:
        res.append(pond.serialize())
    ret = {'items': res, 'page': ponds.page, 'total': ponds.total}
    return jsonify(ret)
