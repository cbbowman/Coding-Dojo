from django.shortcuts import redirect, render
    
def index(request):
    context = {
    }
    return render(request,'index.html', context)

def result(request):
	if request.method == "POST":
		context = {
			"name": request.POST["name"],
			"location": request.POST["location"],
			"favLang": request.POST["favLang"],
			"comment": request.POST["comment"]
		}
	return render(request,'result.html', context)