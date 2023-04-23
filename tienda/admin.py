from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Product
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['names', 'surnames', 'dni', 'phone', 'address', 'email', 'birthdate', 'pub_date']
    search_fields = ['names', 'dni']
    list_filter = ['pub_date']
    list_per_page = True

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer, CustomerAdmin)
