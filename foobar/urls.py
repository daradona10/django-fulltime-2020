from django.urls import path
from .views import get_first_page, get_2020_page, get_welcome_page

urlpatterns = [
    path('', get_first_page, name=''),
    path('year-2020', get_2020_page, name=''),
    path('welcome-2020', get_welcome_page, name='')
]