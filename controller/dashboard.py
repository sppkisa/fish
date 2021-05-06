from flask import Blueprint, render_template, request, jsonify
from sqlalchemy import and_

from model.model import Device, Pond, add, delete, commit

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/dashboard')
def go_dashboard():
    return render_template('dashboard.html')
