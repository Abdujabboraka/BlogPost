from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Blog, BlogCategory, BlogLikes, BlogComment


# Create your views here.

def blog_detail(request, link):
    blog = Blog.objects.get(link=link)
    user = request.user.profile
    is_liked = BlogLikes.objects.filter(blog=blog, user=user).exists()
    categories = BlogCategory.objects.all()
    share_url = request.build_absolute_uri()
    comments = BlogComment.objects.filter(blog=blog).order_by('-created_at')
    context = {
        'blog': blog,
        'categories': categories,
        'share_url': share_url,
        'is_liked': is_liked,
        'comments': comments,
    }
    return render(request, 'homepage/blogdetail.html', context)

@login_required
def like_blog(request, link):
    blog = Blog.objects.get(link=link)
    user = request.user.profile

    # Check if already liked
    liked = BlogLikes.objects.filter(blog=blog, user=user).first()

    if liked:
        # Unlike if already liked
        liked.delete()
        blog.likes = BlogLikes.objects.filter(blog=blog).count()
        blog.save()
    else:
        # Like the blog
        BlogLikes.objects.create(blog=blog, user=user)
        blog.likes = BlogLikes.objects.filter(blog=blog).count()
        blog.save()

    return redirect('blog_detail', link=blog.link)
@login_required
def add_comment(request, link):
    blog = Blog.objects.get(link=link)
    comment_text = request.POST['comment']
    user = request.user.profile
    comment = BlogComment.objects.create(blog=blog, user=user, comment=comment_text)
    comment.save()
    return redirect('blog_detail', link=blog.link)


def category_detail(request, slug):
    category = BlogCategory.objects.get(slug=slug)
    blogs = Blog.objects.filter(category=category)
    context = {
        'category': category,
        'blogs': blogs,
        'categories': BlogCategory.objects.all(),
    }
    return render(request, 'category.html', context)