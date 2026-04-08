from django.shortcuts import render
from blogs.models import Blog, Category

def home(request):
    featured_posts = Blog.objects.filter(featured_post=True, status=1).order_by('-created_at')
    posts = Blog.objects.filter(status=1, featured_post=False).order_by('-created_at')
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request, 'home.html', context)