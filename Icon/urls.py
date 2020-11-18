from django.urls import path

from maplist.views import maplist_detail
from . import views, table, column
from .views import search, signupview, loginview

app_name = 'Icon'

urlpatterns = [

    path('search', search, name='search'),

    path('', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('list/', list, name='list'),

    path('table/new', table.TableCreateView.as_view(), name='table_new'),
    path('table/<int:pk>/column/new', column.ColumnCreateView.as_view(), name='col_new'),

]


# path('',gridview,name='grid'),
