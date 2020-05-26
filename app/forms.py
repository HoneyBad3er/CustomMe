from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class SigninForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class DeviceForm(FlaskForm):
    genres = [("electronic", "electronic"), ("rock", "rock"), ("jazz", "jazz"), ("hip-hop", "hip-hop")]
    headphones_name = StringField('Headphones name', validators=[DataRequired()])
    player_name = StringField('Player device name', validators=[DataRequired()])
    genre = SelectField('Genre', choices=genres)
    submit = SubmitField('Get custom equlaizer!')