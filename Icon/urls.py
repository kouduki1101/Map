from django.urls import path

from . import views, table, column
from .views import search, signup

app_name = 'Icon'

urlpatterns = [

    path('search', search, name='search'),
    path('', search, name='search'),#とりあえずの設定

    path('table/new', table.TableCreateView.as_view(), name='table_new'),
    path('table/<int:pk>/column/new', column.ColumnCreateView.as_view(), name='col_new'),  # 追加
]

# path('',gridview,name='grid'),
