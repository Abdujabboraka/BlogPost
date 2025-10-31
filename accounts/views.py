from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from blog.models import Blog, BlogCategory

@login_required
def add_post_view(request):
    if request.method == 'POST':
        category = request.POST['category']
        title = request.POST['title']
        description = request.POST['description']
        photo = request.FILES['photo']
        owner = request.user.profile

        category_instance = BlogCategory.objects.get(name=category)

        blog = Blog.objects.create(category=category_instance,
                                   title=title,
                                   description=description,
                                   photo=photo,
                                   owner=owner)
        blog.save()
        return redirect('homepage')
    categories = BlogCategory.objects.all()
    context = {'categories': categories}
    return render(request, 'homepage/post.html', context)
