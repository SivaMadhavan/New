from django.shortcuts import render


def page(request):
    return render(request, "myapp/app.html")
