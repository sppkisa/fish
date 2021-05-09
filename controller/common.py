from datetime import timedelta

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, login_user, current_user, logout_user

from model.model import User

common = Blueprint('common', __name__)


@common.route('/', methods=['GET'])
@common.route('/login', methods=['GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('common.index'))
    return render_template('login.html')


@common.route('/logout')  # 登出
@login_required
def logout():
    logout_user()
    return redirect(url_for('common.login'))


@common.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 取表单数据查询用户登陆权限
        user_name = request.form.get('username')
        password = request.form.get('password')
        user = User.get(user_name)  # 从用户数据中查找用户记录
        if user is None:
            flash("用户名不存在")
        else:
            if user.verify_password(password):  # 校验密码
                login_user(user, remember=True, duration=timedelta(minutes=5))  # 创建用户 Session，超时为5分钟
                return render_template('dashboard.html', user_name=user_name)
            else:
                flash("用户名或密码有误")
        return render_template('login.html')
    else:
        return render_template('login.html')
