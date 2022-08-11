from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def abouts(request):
    return render(request, "abouts.html")


def contact(request):
    return render(request, "contact.html")