from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
STATUS_CHOICES = (
    (0, 'Draft'),
    (1, 'Published'),
)
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug= models.SlugField(unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='featured_images/')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=5000)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    featured_post = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
