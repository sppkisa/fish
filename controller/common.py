from flask import Blueprint, render_template

common = Blueprint('common', __name__)


@common.route('/', methods=['GET'])
@common.route('/login', methods=['GET'])
def hello_world():
    return render_template('login.html')


@common.route('/index', methods=['GET', 'POST'])
def go_index():
    return render_template('myindex.html')