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
    #

    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('email/', emailfunc),

    path('table/new', table.TableCreateView.as_view(), name='table_new'),
    path('table/<int:pk>/column/new', column.ColumnCreateView.as_view(), name='col_new'),

]

# path('',gridview,name='grid'),
