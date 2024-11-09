from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.itemListView(), name='item-list'),
    path('items/add/', views.addItemView(), name='add-item'),
]
