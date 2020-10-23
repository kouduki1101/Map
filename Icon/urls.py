from django.urls import path
from .views import signupview,gridview





urlpatterns = [
    path('signup/',signupview,name='signup'),
    path('',gridview,name='grid'),
]