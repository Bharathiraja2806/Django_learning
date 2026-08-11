from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return HttpResponse("hello buddy")

def post(request, id):
    return HttpResponse(f"Post ID {id}")

def firstpage(request):
    return render(request, 'firstpage.html')

def secondpage(request):
    return render(request, 'secondpage.html')

def samplepage(request):
    return redirect(reverse('myapp:old_monk'))

def new_sample_page(request):
    return HttpResponse('this is a old monk redirect page')