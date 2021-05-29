from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import and_
import json

from model.model import Device, Pond, add, delete, commit, Calendar

map_show = Blueprint('map_show', __name__)


@map_show.route('/map_show')
def go_map_show():
    return render_template('map_show.html')
