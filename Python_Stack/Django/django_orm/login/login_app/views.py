from typing import ContextManager
from django.shortcuts import redirect, render, HttpResponse
from .models import User, Book
from django.contrib import messages
import bcrypt

    
def index(request):
	return render(request, "index.html")

def new(request):
	if request.method != "POST":
		return redirect('/')
	# create the user.
	errors = User.objects.new_user_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		context = {
			"first": request.POST['first'],
			"all_books": Book.objects.all()
		}
		password = request.POST['pass']
		pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
		User.objects.create(first=request.POST['first'], last=request.POST['last'], email=request.POST['email'], password=pw_hash)
		return redirect("/success", context)

def login(request):
	if request.method != "POST":
		return redirect('/')
	errors = User.objects.login_user_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		this_user = User.objects.filter(email=request.POST['email'])[0]
		request.session['userid'] = this_user.id
		request.session['first'] = this_user.first
		return redirect("/success")

def success(request):
	if "userid" in request.session:
		return render(request, "success.html")
	else:
		return redirect("/")

def logout(request):
	if request.method != "POST":
		return redirect('/')
	request.session.flush()
	return redirect('/')