# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import BlogPost

class BlogPostSitemap(Sitemap):
    changefreq = "weekly"  # How often the page changes
    priority = 0.8  # Priority of this URL in relation to others

    def items(self):
        # Returns all the objects to include in the sitemap
        return BlogPost.objects.all()

    def lastmod(self, obj):
        # Returns the last modification time for each object
        return obj.updated_at

class StaticViewSitemap(Sitemap):
    priority = 0.5  # Adjust priority as needed
    changefreq = 'monthly'  # Adjust change frequency based on how often these pages change

    def items(self):
        # Return the names of the static views you want to include
        return ['about', 'contact', 'portofolio']

    def location(self, item):
        # Return the URL for each static page
        return reverse(item)