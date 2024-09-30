from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from contact.forms import ContactForm
from django.core.paginator import Paginator
from contact.tasks import send_contact_email
from .models import BlogPost, Category

def index(request):
    featured_articles = {
        'feature1': BlogPost.objects.featured(1),
        'feature2': BlogPost.objects.featured(2),
        'feature3': BlogPost.objects.featured(3),
        'feature4': BlogPost.objects.featured(4),
        'feature5': BlogPost.objects.featured(5)
    }
    posts = BlogPost.objects.exclude(featured_position__in=[1, 2, 3, 4, 5]).filter(is_publish=True)

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/index.html', {'page_obj': page_obj, 'featured_articles': featured_articles})

def about(request):
    return render(request, 'blog/about.html')

def portofolio(request):
    return render(request, 'blog/portofolio.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message to the database
            message = form.save()

            # Send email notification
            send_contact_email.delay(
                name=message.name,
                email=message.email,
                message=message.message
            )

            # Redirect to a success page
            return redirect('contact_success')
    else:   
        form = ContactForm()
    
    context = {
        'form' : form
    }
    return render(request, 'blog/contact.html', context)

def post_detail(request, category_slug, post_slug):
    post = get_object_or_404(BlogPost, slug=post_slug)

     # Get the previous and next posts by the created_at field
    previous_post = BlogPost.objects.filter(created_at__lt=post.created_at).order_by('-created_at').first()
    next_post = BlogPost.objects.filter(created_at__gt=post.created_at).order_by('created_at').first()

    return render(request, 'blog/blog_post.html', {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = BlogPost.objects.order_by('-created_at').filter(category=category, is_publish=True)
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/category_detail.html', {'category': category, 'page_obj': page_obj})

def about(request):
    return render(request, 'blog/about.html')