from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user
from sqlalchemy import and_

from model.model import Device, Pond, add, delete, commit

dashboard = Blueprint('dashboard', __name__)


@dashboard.before_request
@login_required
def before_request():
    if current_user.is_authenticated is False:
        return redirect(url_for('common.login'))


@dashboard.route('/dashboard')
def go_dashboard():
    return render_template('dashboard.html')
