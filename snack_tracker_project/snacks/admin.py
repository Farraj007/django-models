from django.contrib import admin
from .models import Snack

@admin.register(Snack)
class adminthing(admin.ModelAdmin):
    pass

