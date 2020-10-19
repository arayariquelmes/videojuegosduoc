from django.contrib import admin

# Register your models here.
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    readonly_field = ('created','updated')


admin.site.register(Producto, ProductoAdmin)