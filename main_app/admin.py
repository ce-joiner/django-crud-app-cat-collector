from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cat, Feeding

admin.site.register(Cat)
admin.site.register(Feeding)
