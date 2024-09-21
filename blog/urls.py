from django.urls import path
from django.shortcuts import render  # Import render
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_me/', views.about, name='about'),
    path('portofolio/', views.portofolio, name='portofolio'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', lambda request: render(request, 'blog/success.html'), name='contact_success'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    path('<slug:category_slug>/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
