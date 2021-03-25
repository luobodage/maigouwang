from django.contrib import admin
from .models import *


# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ('dog_title', 'salesLocation', 'dog_breed', 'dog_age', 'vaccineSituation', 'dog_price')


admin.site.register(Data, DataAdmin)
