from django import forms

from ExperimentalProject.core.models import Person, Product


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['is_supplier', 'name', 'fancy_name', 'document', 'phone',
                  'email', 'address', 'complement', 'number', 'district',
                  'city', 'uf', 'zipcode']


class ProductForm(forms.ModelForm):
    price = forms.DecimalField(label='Preço', max_digits=15, decimal_places=2, localize=True)

    class Meta:
        model = Product
        fields = '__all__'
