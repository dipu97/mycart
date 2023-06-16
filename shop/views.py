from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'shop/index.html')


def contact(request):
    pass


def about(request):
    pass


def tracking(request):
    pass


def search(request):
    pass


def product(request):
    pass
