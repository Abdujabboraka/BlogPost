from django.urls import path
from .views import profileview

urlpatterns = [
    path('', profileview, name='profile'),
]