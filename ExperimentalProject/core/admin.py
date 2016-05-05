from django.contrib import admin

from ExperimentalProject.core.forms import PersonForm, ProductForm
from ExperimentalProject.core.models import Person, Product


class PersonAdmin(admin.ModelAdmin):
    form = PersonForm
    list_display = ('name', 'fancy_name', 'document_formated', 'phone', 'email', 'is_supplier')


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('name', 'bar_code', 'price_formated', 'ncm', 'inactive')


admin.site.register(Person, PersonAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.site_header = 'Super Simple Sale (3S)'
