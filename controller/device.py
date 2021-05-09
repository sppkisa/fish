from flask import Blueprint, render_template, abort, redirect, url_for
from flask_login import current_user, login_required

from model.model import Device, User

device = Blueprint('device', __name__)


@device.before_request
@login_required
def before_request():
    if current_user.is_authenticated is False:
        return redirect(url_for('common.login'))


@device.route('/device')
def go_device():
    devices = Device.query.all()
    return render_template('device.html', devices=devices)
