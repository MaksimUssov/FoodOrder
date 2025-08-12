from rest_framework import generics
from .models import *
from .serializers import *


class DishListCreateView(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class WorkerListCreateView(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkersSerializer

class CreateOrder(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CreateDishOfOrder(generics.ListCreateAPIView):
    queryset = DishesOfOrder.objects.all()
    serializer_class = DishOfOrderSerializer
