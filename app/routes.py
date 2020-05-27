
from flask import (Blueprint,
                   render_template,
                   request,
                   abort,
                   url_for,
                   flash,
                   redirect
)
from flask_login import (current_user,
                         login_user,
                         logout_user,
                         login_required
)
import pandas as pd
import os
from werkzeug.utils import secure_filename

from app.forms import (LoginForm,
                       DeviceForm,
                       EqSetForm,
                       SignUpForm
)
from app.db_models import UserData, DevicesData
from app.database import db

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_PATH = os.environ.get('UPLOAD_PATH') or \
              os.path.join(basedir, 'static/csv/')

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
    if current_user.is_authenticated:
        return redirect(url_for('custom_me.main'))
    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        new_user = UserData(name=signup_form.username.data,
                            email=signup_form.email.data)
        new_user.set_password(signup_form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('custom_me.login'))
    return render_template('signup.html', title='Sign Up', form=signup_form)


@custom_me.route('/get_eq', methods=['GET', 'POST'])
@login_required
def get_eq():
    device_form = DeviceForm()
    if device_form.validate_on_submit():
        device = DevicesData.query.filter_by(device_name=device_form.headphones_name.data).first()
        if device is None:
            flash('Invalid device name, please try again!')
            return redirect(url_for('custom_me.get_eq'))
        print(device.eq_set_filename)
        return redirect(url_for('custom_me.show_plot', eq_set_name=device.eq_set_filename))
    return render_template('get_eq.html', title='Get equalizer', form=device_form)


@custom_me.route('/set_eq', methods=['GET', 'POST'])
@login_required
def set_eq():
    device_form = EqSetForm()
    if device_form.validate_on_submit():
        if DevicesData.query.filter_by(device_name=device_form.headphones_name.data).first() is None:
            if device_form.eg_file.data:
                eq_data = device_form.eg_file.data
                filename = secure_filename(eq_data.filename)
                eq_data.save(os.path.join(UPLOAD_PATH, filename))
                print(device_form.headphones_name.data)
                print(filename)
                new_device = DevicesData(device_name=device_form.headphones_name.data,
                                         eq_set_filename=filename,
                                         device_info="Headphones",
                                         user_id=current_user.get_id())
                db.session.add(new_device)
                db.session.commit()
                return redirect(url_for('custom_me.main'))
        else:
            return redirect(url_for('custom_me.main'))
    return render_template('set_eq.html', title='Set equalizer', form=device_form)


@custom_me.route('/show_plot', methods=['GET', 'POST'])
def show_plot():
    df = pd.read_csv(os.path.join(UPLOAD_PATH, request.args.get('eq_set_name')))
    return df.to_html()
