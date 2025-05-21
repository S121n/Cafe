from django.urls import path
from .views import customer_signup_view, customer_login_view, customer_logout_view, profile_view

urlpatterns = [
    path('signup/', customer_signup_view, name='signup'),
    path('login/', customer_login_view, name='login'),
    path('logout/', customer_logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),

]
