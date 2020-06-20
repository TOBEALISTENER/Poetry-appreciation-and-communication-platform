from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def Login(request):
    return render(request, "sign_in.html")


def Register(request):
    return render(request, "sign_up.html")
