from django.shortcuts import redirect, render 
from django.utils.crypto import get_random_string
    
def index(request):
	if 'random_word' not in request.session:	
		request.session['random_word']=get_random_string(length=14)
	if 'counter' not in request.session:
		request.session['counter']=1
	return render(request,'index.html')

def generate(request):
	request.session['random_word']=get_random_string(length=14)
	request.session['counter']+=1
	return redirect('/random_word')

def reset(request):
	request.session['counter']=1
	return redirect('/random_word')
