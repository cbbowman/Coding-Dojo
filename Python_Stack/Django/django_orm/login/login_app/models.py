from django.db import models
import re, bcrypt

class UserManager(models.Manager):
	def new_user_validator(self, postData):
		errors = {}
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if len(postData['first']) < 2:
			errors["first"] = "First name should be at least 2 characters"
		if not str.isalpha(postData['first']):
			errors["first_alpha"] = "First name must only contain letters"
		if len(postData['last']) < 2:
			errors["last"] = "Last name should be at least 2 characters"
		if not str.isalpha(postData['last']):
			errors["last_alpha"] = "Last name must only contain letters"
		if not EMAIL_REGEX.match(postData['email']):
			errors["email"] = "Email must be valid form"
		if len(User.objects.filter(email=postData['email'])):
			errors["unique"] = "A user with that email already exists"
		if not postData['pass'] == postData['pass_confirm']:
			errors["pass_match"] = "Passwords must match"
		if len(postData['pass']) < 8:
			errors["pass_length"] = "Password should be at least 8 characters"
		return errors

	def login_user_validator(self, postData):
		errors = {}
		if not len(postData['email']):
			errors["email_blank"] = "Email must not be blank"
		if not len(postData['pass']):
			errors["pw_blank"] = "Password must not be blank"
		if not len(User.objects.filter(email=postData['email'])):
			errors["no_user"] = "Invalid email"
		else:
			this_user = User.objects.filter(email=postData['email'])
			# this_hash = this_user.password
			if not bcrypt.checkpw(postData['pass'].encode(), this_user[0].password.encode()):
				errors["wrong_pw"] = "Incorrect password"

		return errors


class User(models.Model):
	first = models.CharField(max_length=255)
	last = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()