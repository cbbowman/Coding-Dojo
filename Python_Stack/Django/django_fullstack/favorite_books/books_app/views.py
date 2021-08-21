from typing import ContextManager
from django.shortcuts import redirect, render, HttpResponse
from .models import User, Book
from django.contrib import messages
import bcrypt

    
def index(request):
	return render(request, "index.html")

def register(request):
	if request.method != "POST":
		return redirect('/')
	# create the user.
	errors = User.objects.new_user_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		password = request.POST['pass']
		pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
		new_user = User.objects.create(first=request.POST['first'], last=request.POST['last'], email=request.POST['email'], password=pw_hash)
		# context = {
		# 	"user": new_user
		# }
		request.session["user"] = new_user.id
		return redirect("/books")

def login(request):
	if request.method != "POST":
		return redirect('/')
	errors = User.objects.login_user_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		this_user=User.objects.filter(email=request.POST['email'])[0]
		request.session["user"] = this_user.id
		# this_user = User.objects.filter(email=request.POST['email'])[0]
		# request.session['userid'] = this_user.id
		# request.session['first'] = this_user.first
		return redirect("/books")

def books(request):
	if "user" in request.session:
		this_user=User.objects.filter(id=request.session["user"])[0]
		context = {
			"all_books": Book.objects.all(),
			"user": this_user,
			"all_favorites": this_user.favorites.all()
		}
		return render(request, "all_books.html", context)
	else:
		return redirect("/")

def add(request):
	if request.method != "POST":
		return redirect('/')
	errors = User.objects.add_book_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		this_user=User.objects.filter(id=request.session["user"])[0]
		new_book=Book.objects.create(title=request.POST['title'], description=request.POST['description'], added_by=this_user)
		this_user.favorites.add(new_book)
		return redirect('/books')

def book(request, book_id):
	this_book=Book.objects.filter(id=book_id)[0]
	this_user=User.objects.filter(id=request.session['user'])[0]
	context = {
		"book": this_book,
		"user": this_user,
		"all_favorites": this_book.favorites.all()
	}
	return render(request, "book.html", context)

def update(request, book_id):
	if request.method != "POST":
		return redirect('/')
	errors = User.objects.add_book_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	this_book = Book.objects.filter(id=book_id)[0]
	if request.session["user"] != this_book.added_by.id:
		return redirect('/')
	else:
		# this_book.update(title=request.POST['title'], description=request.POST['description'])
		this_book.title = request.POST['title']
		this_book.description = request.POST['description']
		this_book.save()
		return redirect('/books')

def delete(request, book_id):
	if request.method != "POST":
		return redirect('/')
	this_book = Book.objects.filter(id=book_id)[0]
	if request.session["user"] != this_book.added_by.id:
		return redirect('/')
	else:
		this_book.delete()
		return redirect('/books')

def favorite(request, book_id):
	if request.method != "POST":
		return redirect('/')
	else:
		this_user=User.objects.filter(id=request.session['user'])[0]
		this_book=Book.objects.filter(id=book_id)[0]
		if this_user in this_book.favorites.all():
			this_book.favorites.remove(this_user)
		else:
			this_book.favorites.add(this_user)
		return redirect('/books')

def logout(request):
	if request.method != "POST":
		return redirect('/')
	request.session.flush()
	return redirect('/')