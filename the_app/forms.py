from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from the_app.models import User

class LoginForm(FlaskForm):
	
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
	
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email Address', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Password Again', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('This username already exists')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('This email already exists!')

	#doing the following code was a failure:: 

	#def validate_password2(self, password2):
		

	# 	if password2 != password:
	# 		raise ValidationError("The passwords don't match!")

	# somehow I have to pass in password.data into this function.

class EditProfileForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	about_me = TextAreaField('About Me:', validators=[Length(min=0, max=140)])
	submit = SubmitField('Submit')