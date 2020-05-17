from django.shortcuts import render, redirect
from .models import Blog
import time
# Create your views here.
def index(request):
    movie = Blog.objects.filter(category='movie').count()
    drama = Blog.objects.filter(category='drama').count()
    entertain = Blog.objects.filter(category='entertain').count()
    return render(request, 'index.html', {'movie':movie, 'drama':drama, 'entertain':entertain})

def detail(request, primary_key):
    article = Blog.objects.get(pk=primary_key)
    return render(request, 'detail.html', {'article':article})

def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Blog.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            time = time.strftime('%c', time.localtime(time.time()))
        )
        return redirect(detail, new_article.pk)
    else:
        return render(request, 'new.html')

def movie(request):
    movie = Blog.objects.filter(category='movie')
    return render(request, 'movie.html', {'movie':movie})

def drama(request):
    drama = Blog.objects.filter(category='drama')
    return render(request, 'drama.html', {'drama':drama})

def entertain(request):
    entertain = Blog.objects.filter(category='entertain')
    return render(request, 'entertain.html', {'entertain':entertain})
