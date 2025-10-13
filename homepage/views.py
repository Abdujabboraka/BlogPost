from django.shortcuts import render
from blog.models import BlogCategory, Blog

# Create your views here.


def homepage(request):
    categories = BlogCategory.objects.all()
    blogs = Blog.objects.all()
    context = {
        'categories': categories,
        'blogs': blogs,
    }
    return render(request, 'homepage/homepage.html', context)

