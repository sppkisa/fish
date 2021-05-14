from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import and_
import json

from model.model import Device, Pond, add, delete, commit, Calendar

calendar = Blueprint('calendar', __name__)


@calendar.route('/calendar')
def go_calendar():
    return render_template('calendar.html')


@calendar.route('/submit_calendar', methods=['POST'])
def submit_calendar():
    time = request.values.get('time')
    pond_id = request.values.get('pond_id')

    operation1 = request.values.getlist("operation")
    string_operation = operation1[0]
    operation = string_operation.split(',')

    other = request.values.get('other')
    user_id = 1

    if 'food' in operation:
        food = 1
    else:
        food = 0
    if 'vaccine' in operation:
        vaccine = 1
    else:
        vaccine = 0
    if 'clean_water' in operation:
        clean_water = 1
    else:
        clean_water = 0
    if 'add_fish' in operation:
        add_fish = 1
    else:
        add_fish = 0
    if 'kill_insect' in operation:
        kill_insect = 1
    else:
        kill_insect = 0
    if 'disinfect' in operation:
        disinfect = 1
    else:
        disinfect = 0

    calendar = Calendar(time, food, pond_id, vaccine, clean_water, add_fish, kill_insect, disinfect, other, user_id)
    add(calendar)
    return 'ok'

