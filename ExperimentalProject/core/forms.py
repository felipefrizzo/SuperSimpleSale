from django import forms

from ExperimentalProject.core.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['is_supplier', 'name', 'fancy_name', 'document', 'phone',
                  'email', 'address', 'complement', 'number', 'district',
                  'city', 'uf', 'zipcode']
