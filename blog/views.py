from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Category

def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def portofolio(request):
    return render(request, 'blog/portofolio.html')

def contact(request):
    return render(request, 'blog/contact.html')

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = BlogPost.objects.filter(category=category)
    return render(request, 'blog/category_detail.html', {'category': category, 'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def projects(request):
    return render(request, 'blog/projects.html')

def contact(request):
    return render(request, 'blog/contact.html')