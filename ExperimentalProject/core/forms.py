from django import forms

from ExperimentalProject.core.models import Person, Product


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['is_supplier', 'name', 'fancy_name', 'document', 'phone',
                  'email', 'address', 'complement', 'number', 'district',
                  'city', 'uf', 'zipcode']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
