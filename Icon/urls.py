from django.urls import path
from .views import signupview,gridview,loginview,listview





urlpatterns = [
    path('',signupview,name='signup'),
    path('login/',loginview,name="login"),
    path('list/',listview,name='list'),
    # path('',gridview,name='grid'),
]