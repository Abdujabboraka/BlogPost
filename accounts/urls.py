from django.urls import path
from .views import add_post_view

urlpatterns = [
    path("add_post/", add_post_view, name='add_post'),
]