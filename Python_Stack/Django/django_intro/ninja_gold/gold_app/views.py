from typing import ContextManager
from django.shortcuts import redirect, render 
import random
    
def index(request):
	if 'gold_total' not in request.session:
		request.session['gold_total']=0
	request.session['gold'] = 0
	request.session['farm']=random.randint(10, 20)
	request.session['cave']=random.randint(5, 10)
	request.session['house']=random.randint(2, 5)
	request.session['casino']=random.randint(-50, 50)
	return render(request,'index.html')

def process_money(request):
	print(request.session['gold'])
	print(request.session['cave'])
	print(request.session['farm'])
	print(request.session['house'])
	print(request.session['casino'])
	print(request.session['gold_total'])
	request.session['gold_total']+=request.POST['gold']
	return redirect('/')
