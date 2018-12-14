from the_app import app
from flask import render_template, flash, redirect
from the_app.forms import myForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Mu'}

	posts = [
		{'author': {'username': 'Jonathan', 'nickname': 'John'},
		'body': 'Looks like a great day'
		},
		{'author': {'username': 'Homer', 'nickname': 'Hombre'},
		'body': 'Definitely a lot better than yesterday'
		}
	]

	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
		form = myForm()
		if form.validate_on_submit():
			flash('Login requested for user {}, remember me is {}'.format(form.username.data, form.remember_me.data))
			return redirect('/index')

		return render_template('login.html', title='Sign In', form=form)	