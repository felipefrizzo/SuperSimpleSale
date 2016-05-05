from django.contrib import admin

from ExperimentalProject.core.forms import PersonForm
from ExperimentalProject.core.models import Person


class PersonAdmin(admin.ModelAdmin):
    form = PersonForm
    list_display = ('name', 'document_formated', 'phone', 'email', 'is_supplier')


admin.site.register(Person, PersonAdmin)
