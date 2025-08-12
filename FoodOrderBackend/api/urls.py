from django.urls import path
from .views import *

urlpatterns = [
    path('dishes/', DishListCreateView.as_view()),
    path('workers/', WorkerListCreateView.as_view()),
    path('order/', CreateOrder.as_view()),
    path('dishoforder/', CreateDishOfOrder.as_view()),
]