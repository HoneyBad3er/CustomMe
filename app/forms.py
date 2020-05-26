from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,
                     BooleanField, SubmitField,
                     SelectField, FileField
                     )
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.validators import (DataRequired, Email,
                                regexp, ValidationError,
                                EqualTo
                                )
from app.db_models import UserData


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = UserData.query.filter_by(name=username.data).first()
        if user is not None:
            raise ValidationError('This username is handled!.')

    def validate_email(self, email):
        user = UserData.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This email is handled!')


class DeviceForm(FlaskForm):
    genres = [("electronic", "electronic"), ("rock", "rock"), ("jazz", "jazz"), ("hip-hop", "hip-hop")]
    headphones_name = StringField('Headphones name', validators=[DataRequired()])
    player_name = StringField('Player device name', validators=[DataRequired()])
    genre = SelectField('Genre', choices=genres)
    submit = SubmitField('Get custom equlaizer!')


class EqSetForm(FlaskForm):
    genres = [("electronic", "electronic"), ("rock", "rock"), ("jazz", "jazz"), ("hip-hop", "hip-hop")]
    headphones_name = StringField('Headphones name', validators=[DataRequired()])
    player_name = StringField('Player device name', validators=[DataRequired()])
    genre = SelectField('Genre', choices=genres)
    eg_file = FileField('Equalizer File', validators=[FileRequired(), FileAllowed(['csv'], 'Please csv')])
    submit = SubmitField('Set custom equlaizer!')