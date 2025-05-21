from django.urls import path
from .views import menu_view
from . import views

urlpatterns = [
    path('', menu_view, name='menu'),
]