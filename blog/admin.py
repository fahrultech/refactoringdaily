# admin.py

from django.contrib import admin
from .models import BlogPost, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured_position', 'created_at', 'updated_at')
    list_filter = ('featured_position', 'category', 'created_at')
    search_fields = ('title', 'content', 'meta_description')
    prepopulated_fields = {'slug': ('title',)}
    actions = ['clear_featured']

    def clear_featured(self, request, queryset):
        queryset.update(featured_position=0)
    clear_featured.short_description = "Clear selected articles from featured positions"
