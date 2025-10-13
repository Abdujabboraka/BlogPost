from django.urls import path
from .views import blog_detail, like_blog, add_comment, category_detail

urlpatterns = [
    path('<str:slug>/', category_detail, name='category_detail'),
    path('blog/<str:link>/', blog_detail, name='blog_detail'),
    path('like/<str:link>/', like_blog, name='like_blog'),
    path('add_comment/<int:pk>/', add_comment, name='add_comment'),
]