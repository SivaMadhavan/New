from django.shortcuts import render


# Create your views here.
def page(request):
    return render(request, "myapp/app.html")
