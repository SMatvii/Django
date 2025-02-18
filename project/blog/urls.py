from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('create-item/', views.create_item, name='create_item'),
    path('category/<int:category_id>/delete/', views.delete_category, name='delete_category'),
    path('category/<int:category_id>/', views.category_view, name='category_view'),
    path('item/<int:item_id>/delete/', views.delete_item, name='delete_item'),
    path('create/', views.create_item, name='create_item'),
]