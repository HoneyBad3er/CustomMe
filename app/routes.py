from flask import (
    Blueprint,
    render_template,
    request,
    abort,
    url_for
)

from app.forms import LoginForm

custom_me = Blueprint('custom_me', __name__, template_folder='templates')


@custom_me.route('/')
@custom_me.route('/main', methods=['GET'])
def main():
    # Mock user
    user = {'username': 'Marat'}
    return render_template('main.html', title='Home', user=user, login_link='/login')


@custom_me.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    return render_template('login.html', title='Log In', form=login_form)


@custom_me.route('/signin', methods=['GET', 'POST'])
def signin():
    return "Signin page"


# @custom_me.route('/user/<username>')
# # @login_required
# def user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     return render_template('user.html', user=user)
