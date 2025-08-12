from django.contrib import admin
from api.models import *

admin.site.register(Worker)
admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(DishesOfOrder)
admin.site.register(Section)