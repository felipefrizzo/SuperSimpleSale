from django.contrib import admin
from ExperimentalProject.core.forms import PersonForm, ProductForm, PaymentForm
from ExperimentalProject.core.models import Person, Product, Payment, Sale, SaleItem


class PersonAdmin(admin.ModelAdmin):
    form = PersonForm
    list_display = ('name', 'fancy_name', 'document_formated', 'phone', 'email', 'is_supplier')
    search_fields = ('name', 'document')
    list_filter = ('is_supplier', 'city', 'district', 'uf')


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('name', 'bar_code', 'price_formated', 'ncm', 'inactive')
    search_fields = ('name', 'bar_code', 'ncm')
    list_filter = ('inactive', 'ncm')


class PaymentAdmin(admin.ModelAdmin):
    form = PaymentForm
    list_display = ('name', 'addtions')
    search_fields = ('name',)


class SaleItemAdmin(admin.TabularInline):
    model = SaleItem
    extra = 1
    
    
class SalaAdmin(admin.ModelAdmin):
    fieldsets = [
        (Nome, {'fields': ['client']}),
        (Nome, {'fields': ['payment']}),
        ]
    inlines = [SaleItemAdmin]
    model = Sale
        
    list_display = ('person', 'get_total', 'payment', 'created_at')
        

admin.site.register(Payment, PaymentAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.site_header = 'Super Simple Sale (3S)'
