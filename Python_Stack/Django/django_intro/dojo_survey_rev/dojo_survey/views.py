from django.shortcuts import redirect, render
    
def index(request):
    return render(request,'index.html')

def submit(request):
	request.session['name']=request.POST['name']
	request.session['location']=request.POST['location']
	request.session['favLang']=request.POST['favLang']
	request.session['comment']=request.POST['comment']
	return redirect('/confirmation')

def confirmation(request):
    return render(request,'confirmation.html')

# def result(request):
# 	if request.method == "POST":
# 		context = {
# 			"name": request.POST ["name"],
# 			"location": request.POST["location"],
# 			"favLang": request.POST["favLang"],
# 			"comment": request.POST["comment"]
# 		}
# 	return render(request,'result.html', context)