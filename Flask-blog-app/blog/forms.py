from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, Regexp
from blog.models import User

class RegistrationForm(FlaskForm):
  username = StringField('Username*',validators=[DataRequired(),Length(min=3,max=15)], render_kw={"placeholder":"Username"})
  Forename = StringField('Forename*', validators=[DataRequired()], render_kw={"placeholder":"First name"})
  Surname = StringField('Surname', render_kw={"placeholder":"Surname"})
  email = StringField('Email*',validators=[DataRequired(),Email()], render_kw={"placeholder":"Email"})
  password = PasswordField('Password*',validators=[DataRequired(),Regexp('^.{6,10}$',message='Password should be between 6 and 10 characters long.')], render_kw={"placeholder":"Must be 6-10 characters long"})

  confirm_password = PasswordField('Confirm Password*',validators=[DataRequired(),EqualTo('password', message='Passwords need to match')], render_kw={"placeholder":"Confirm password"})
  submit = SubmitField('Register')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
      raise ValidationError('Username taken. Try again!')

  def validate_email(self,email):
    user = User.query.filter_by(email=email.data).first()
    if user is not None:
      raise ValidationError('This email already belongs to an account.')

class LoginForm(FlaskForm):
  email = StringField('Email',validators=[DataRequired(),Email()], render_kw={"placeholder":"Email"})
  password = PasswordField('Password',validators=[DataRequired()], render_kw={"placeholder":"Password"})
  submit = SubmitField('Login')

class CommentForm(FlaskForm):
  comment = StringField('Comment',validators=[InputRequired()], render_kw={"placeholder":"Type a comment..."})
  submit = SubmitField('Post comment')

class FavouriteForm(FlaskForm):
  submit = SubmitField('★')
