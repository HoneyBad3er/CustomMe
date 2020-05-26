
from flask import (
    Blueprint,
    render_template,
    request,
    abort,
    url_for,
    flash,
    redirect
)
from flask_login import current_user, login_user, logout_user
import pandas as pd

from app.forms import LoginForm, DeviceForm
from app.db_models import UserData, DevicesData

custom_me = Blueprint('custom_me', __name__, template_folder='templates')


@custom_me.route('/')
@custom_me.route('/main', methods=['GET'])
def main():
    return render_template('main.html', title='Home', login_link='/login')


@custom_me.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('custom_me.main'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = UserData.query.filter_by(name=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid username or password, please try again!')
            return redirect(url_for('custom_me.login'))
        login_user(user, remember=login_form.remember_me.data)
        return redirect(url_for('custom_me.main'))
    return render_template('login.html', title='Log In', form=login_form)


@custom_me.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('custom_me.main'))


@custom_me.route('/signup', methods=['GET', 'POST'])
def signup():
    return "Sign Up page"


@custom_me.route('/get_eq', methods=['GET', 'POST'])
def get_eq():
    device_form = DeviceForm()
    if device_form.validate_on_submit():
        device = DevicesData.query.filter_by(device_name=device_form.headphones_name.data).first()
        if device is None:
            flash('Invalid device name, please try again!')
            return redirect(url_for('custom_me.get_eq'))
        return redirect(url_for('custom_me.show_plot', eq_set_name=device.id))
    return render_template('get_eq.html', title='Get equalizer', form=device_form)


@custom_me.route('/show_plot', methods=['GET', 'POST'])
def show_plot():
    df = pd.read_csv(request.args.get('eq_set_name'))
    return df.to_html()


# @custom_me.route('/user/<username>')
# # @login_required
# def user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     return render_template('user.html', user=user)
