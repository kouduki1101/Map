from django.urls import path
from . import views, table, column
from .views import search, signupview, loginview, homeview, forgetview, emailfunc
from django.contrib.auth import views as auth_views

app_name = 'Icon'

urlpatterns = [

    path('search', search, name='search'),
    path('', homeview, name='home'),
    path('forget', forgetview, name='forget'),
    path('signup', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('list/', list, name='list'),
    path('change_password/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('email/', emailfunc),

    path('table/new', table.TableCreateView.as_view(), name='table_new'),
    path('table/<int:pk>/column/new', column.ColumnCreateView.as_view(), name='col_new'),

]

# path('',gridview,name='grid'),
