from django.shortcuts import render

def Homepage(request, *args, **kwargs):
    return render(request, "index.html")