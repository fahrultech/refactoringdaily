from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class BlogPostQuerySet(models.QuerySet):
    def featured(self, position):
        return self.filter(featured_position=position).first()  # Get the article for a specific featured position

class BlogPost(models.Model):
    FEATURED_CHOICES = [
        (0, 'Not Featured'),
        (1, 'Feature 1'),
        (2, 'Feature 2'),
        (3, 'Feature 3'),
        (4, 'Feature 4'),
        (5, 'Feature 5'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    content = RichTextField()
    meta_description = models.CharField(max_length=160, blank=True)
    featured_position = models.PositiveSmallIntegerField(choices=FEATURED_CHOICES, default=0)  # New field for featured slot
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Use the custom queryset for BlogPost
    objects = BlogPostQuerySet.as_manager()

    def save(self, *args, **kwargs):
        # Automatically generate slug from title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title