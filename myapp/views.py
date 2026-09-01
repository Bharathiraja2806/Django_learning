from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
import logging
from myapp.models import Post


# heello = [
#     {"id": 1, "name": "John", "age": 30},
#     {"id": 2, "name": "Jane", "age": 25},
#     {"id": 3, "name": "Bob", "age": 40},
# ]

# Create your views here.
def index(request):
    data = Post.objects.all()
    logger = logging.getLogger('Testing')
    logger.debug('summa oru debug message')
    return render(request, "index.html", {"posts": data})

def post(request, id):
    # data = next((item for item in heello if item["id"] == int(id)), None)
    try:
        data = Post.objects.get(slug=id) #either we can give id =  , or pk = id, both are same, but pk (primary key) is more generic, as it can be used for any primary key, not just id
        logger = logging.getLogger('Testing')
        logger.debug(f"the post variable is {data}")

    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
    return render(request, "post.html", {"post" : data})

def firstpage(request):
    return render(request, 'firstpage.html')

def secondpage(request):
    return render(request, 'secondpage.html')

def samplepage(request):
    return redirect(reverse('myapp:old_monk'))

def new_sample_page(request):
    return HttpResponse('this is a old monk redirect page')