from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import and_

from model.model import Device, Pond, add, delete, commit, User

user = Blueprint('user', __name__)


@user.route('/user')
def go_user():
    users = User.query.all()
    return render_template('user.html', users=users)


@user.route('/save_user', methods=['POST'])
def save_user():
    page = 1
    # 接收页码
    if request.values.get('page'):
        page = int(request.values.get('page'))
    id = request.form.get('id')
    name = request.form.get('name')
    password = request.form.get('password')
    type = request.form.get('type')
    phone = request.form.get('phone')
    wechat = request.form.get('wechat')

    if id:
        User.query.filter(User.user_id == id).update({'user_name': name, 'user_password': password, 'user_type': type, 'user_phone': phone, 'user_wechat': wechat})
        commit()
    else:
        user = User(name, password, type, phone, wechat)
        add(user)
    users = User.query.paginate(page=page, per_page=10)
    return toJson(users)


@user.route('/select_user', methods=['GET', 'POST'])
def select_user():
    page = 1
    # 接收页码
    if request.values.get('page'):
        page = int(request.values.get('page'))
    name = request.values.get('name')
    password = request.values.get('password')
    type = request.values.get('type')
    phone = request.values.get('phone')
    wechat = request.values.get('wechat')
    query = User.query

    if name:
        query = query.filter(and_(User.user_name.like('%{name}%'.format(name=name))))
    if password:
        query = query.filter(and_(User.user_password.like('%{password}%'.format(password=password))))
    if type:
        query = query.filter(and_(User.user_type.like('%{type}%'.format(type=type))))
    if phone:
        query = query.filter(and_(User.user_phone.like('%{phone}%'.format(phone=phone))))
    if wechat:
        query = query.filter(and_(User.user_wechat.like('%{wechat}%'.format(wechat=wechat))))
    # 重新查表分页
    users = query.paginate(page=page, per_page=10)
    return toJson(users)


@user.route('/delete_user', methods=['POST'])
def delete_user():
    page = 1
    # 接收页码
    if request.values.get('page'):
        page = int(request.values.get('page'))
    user_id = request.values.get('id')
    obj = User.query.filter(User.user_id == user_id).first()
    delete(obj)
    users = User.query.paginate(page=page, per_page=10)
    return toJson(users)


def toJson(users):
    res = []
    for user in users.items:
        res.append(user.serialize1())
    ret = {'items': res, 'page': users.page, 'total': users.total}
    return jsonify(ret)
