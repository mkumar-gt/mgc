2018-12-30 13:39:13,558 INFO: Microblog startup [in /Users/mk/Downloads/Py/f/microblog/the_app/__init__.py:46]
2018-12-30 13:39:22,026 ERROR: Exception on /edit_profile [GET] [in /Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py:1761]
Traceback (most recent call last):
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask_login/utils.py", line 261, in decorated_view
    return func(*args, **kwargs)
  File "/Users/mk/Downloads/Py/f/microblog/the_app/routes.py", line 83, in edit_profile
    form = EditProfileForm(current_user.username)
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/wtforms/form.py", line 212, in __call__
    return type.__call__(cls, *args, **kwargs)
  File "/Users/mk/Downloads/Py/f/microblog/the_app/forms.py", line 47, in __init__
    super(EditProfileForm, self).__init__(*args, **kwargs)
NameError: name 'kwargs' is not defined
2018-12-30 13:39:33,960 ERROR: Exception on /edit_profile [GET] [in /Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py:1761]
Traceback (most recent call last):
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask_login/utils.py", line 261, in decorated_view
    return func(*args, **kwargs)
  File "/Users/mk/Downloads/Py/f/microblog/the_app/routes.py", line 83, in edit_profile
    form = EditProfileForm(current_user.username)
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/wtforms/form.py", line 212, in __call__
    return type.__call__(cls, *args, **kwargs)
  File "/Users/mk/Downloads/Py/f/microblog/the_app/forms.py", line 47, in __init__
    super(EditProfileForm, self).__init__(*args, **kwargs)
NameError: name 'kwargs' is not defined
2018-12-30 13:45:13,978 INFO: Microblog startup [in /Users/mk/Downloads/Py/f/microblog/the_app/__init__.py:46]
2018-12-30 13:45:32,228 ERROR: Exception on /edit_profile [POST] [in /Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py:1761]
Traceback (most recent call last):
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/_compat.py", line 35, in reraise
    raise value
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask/app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask_login/utils.py", line 261, in decorated_view
    return func(*args, **kwargs)
  File "/Users/mk/Downloads/Py/f/microblog/the_app/routes.py", line 84, in edit_profile
    if form.validate_on_submit():
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/flask_wtf/form.py", line 101, in validate_on_submit
    return self.is_submitted() and self.validate()
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/wtforms/form.py", line 310, in validate
    return super(Form, self).validate(extra)
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/wtforms/form.py", line 152, in validate
    if not field.validate(self, extra):
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/wtforms/fields/core.py", line 206, in validate
    stop_validation = self._run_validation_chain(form, chain)
  File "/Users/mk/Downloads/Py/f/microblog/virtualenv1/lib/python3.7/site-packages/wtforms/fields/core.py", line 226, in _run_validation_chain
    validator(form, self)
TypeError: validate_username() takes 0 positional arguments but 2 were given
