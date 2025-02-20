from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,"index_html.html")

def home(request):
    name = "japar"
    surname = "Jeenbekov"
    context = {
      "name":name,
      "surname":surname,



    }

    return render(request,"home.html",context)


