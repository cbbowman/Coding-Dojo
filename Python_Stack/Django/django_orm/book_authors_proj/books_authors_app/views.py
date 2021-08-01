from typing import ContextManager
from django.shortcuts import redirect, render 
# from .models import User
    
def index(request):
	context = {
		# "all_the_users": User.objects.all()
		}
	return render(request,'index.html',context)