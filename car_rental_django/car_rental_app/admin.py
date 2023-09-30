from django.contrib import admin
from .models import *
admin.site.register(credentials)
admin.site.register(places)
admin.site.register(car_detail)
admin.site.register(rental_detail)
admin.site.register(rental_history)