from flask import (
    Blueprint,
    render_template,
    request,
    abort,
    url_for
)


custom_me = Blueprint('custom_me', __name__, template_folder='templates')


@custom_me.route('/')
def main():
    return "Main page"


@custom_me.route('/login', methods=['GET', 'POST'])
def login():
    return "Login page"


@custom_me.route('/anutka', methods=['GET', 'POST'])
def anutka():
    return "ann page"
