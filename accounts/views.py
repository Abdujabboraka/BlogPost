from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import  UserProfile
from blog.models import Blog, BlogCategory, BlogComment, BlogLikes
# Create your views here.

def profileview(request):
    userprofile = UserProfile.objects.get(user=request.user)
    userblogs = Blog.objects.filter(owner=request.user).order_by('-created_at')
    categories = BlogCategory.objects.all()
    context = {
        'userprofile': userprofile,
        'userblogs': userblogs,
        'categories': categories,
    }
    return render(request, 'accounts/profile.html', context)