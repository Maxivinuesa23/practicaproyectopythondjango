from django.shortcuts import render

# Create your views here.

def index(request):
    context = {"mensaje": "Bienvenidos a todos a esta pagina con Django"}
    return render(request, "myapp/index.html", context)