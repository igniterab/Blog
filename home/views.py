from django.shortcuts import render , redirect
from django.http import HttpResponse 
from . models import Blog
from . form import *

# Create your views here.


def home(request):
    blog = Blog.objects.all().order_by('date')
    return render(request,"home.html",{'blog':blog})

def full(request,slug):
    #return HttpResponse(slug)
    article = Blog.objects.get(slug=slug)
    return render(request,"article.html",{'article':article})


def create(request):
    if request.method == 'POST': 
        form = CreateBlog(request.POST, request.FILES) 
  
        if form.is_valid(): 
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()

            return redirect('home:home') 
    else:

        form = CreateBlog() 

  
    return render(request,"create.html",{'form':form})