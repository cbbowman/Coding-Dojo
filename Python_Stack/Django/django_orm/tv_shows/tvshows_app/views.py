from typing import ContextManager
from django.shortcuts import redirect, render 
from .models import Show
    
def index(request):
	return redirect("/shows")

def new_show(request):
	return render(request, "new.html")

def add_show(request):
	if request.method != "POST":
		return redirect("/shows/new")
	# create the show.
	Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release'], description=request.POST['description'])
	return redirect("/shows")

def show(request, show_id):
	this_show = Show.objects.get(id=show_id)
	context={
		'title': this_show.title,
		'network': this_show.network,
		'release': this_show.release_date,
		'description': this_show.description,
		'updated': this_show.updated_at,
	}

	return render(request, "show.html", context)

def all_shows(request):
	context = {
		"all_the_shows": Show.objects.all()
	}
	return render(request, "shows.html", context)

def edit_show(request, show_id):
	this_show = Show.objects.get(id=show_id)
	context={
		'showid': show_id,
		'title': this_show.title,
		'network': this_show.network,
		'release': this_show.release_date,
		'description': this_show.description,
	}
	return render(request, "edit.html", context)

def update_show(request, show_id):
	if request.method != "POST":
		return render(request, "shows.html")
	# update the show
	this_show = Show.objects.get(id=show_id)
	this_show.title=request.POST['title']
	this_show.network=request.POST['network']
	this_show.release_date=request.POST['release']
	this_show.description=request.POST['description']
	this_show.save()
	return redirect("/shows")

def delete_show(request, show_id):
	if request.method != "POST":
		return redirect("/shows")
	# delete the show
	this_show = Show.objects.get(id=show_id)
	this_show.delete()
	return redirect("/shows")

