from flask import Blueprint, render_template

from model.model import Device

device = Blueprint('device', __name__)


@device.route('/device')
def go_device():
    devices = Device.query.all()
    return render_template('device.html', devices=devices)
