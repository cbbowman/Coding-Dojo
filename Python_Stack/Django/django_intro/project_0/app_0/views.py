from django.shortcuts import render
    
def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)


def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog number: {number}")

def destroy(request, number):
    return redirect('/')
