from django.db import models
from django.shortcuts import resolve_url
from django.utils.formats import number_format

from ExperimentalProject.utils.lists import UF_LIST


class Address(models.Model):
    address = models.CharField('rua', max_length=255)
    complement = models.CharField('complemento', max_length=255, blank=True)
    number = models.PositiveIntegerField('numero')
    district = models.CharField('bairro', max_length=255)
    city = models.CharField('cidade', max_length=255)
    uf = models.CharField('estado', max_length=2, choices=UF_LIST)
    zipcode = models.CharField('CEP', max_length=10)

    class Meta:
        abstract = True


class Person(Address):
    is_supplier = models.BooleanField('fornecedor')
    name = models.CharField('nome', max_length=255)
    fancy_name = models.CharField('nome fantasia/apelido', max_length=255)
    document = models.CharField('CNPJ/CPF', max_length=18, unique=True, null=True)
    phone = models.CharField('telefone', max_length=18, blank=True, null=True)
    email = models.EmailField('e-mail', max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'cliente/fornecedor'
        verbose_name_plural = 'clientes/fornecedores'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('person', self.pk)

    def document_formated(self):
        formated = '{}.{}.{}/{}-{}'.format(self.document[0:2], self.document[2:5], self.document[5:8],
                                           self.document[8:12], self.document[12:14]) \
            if self.document.__len__() > 12 else '{}.{}.{}-{}'.format(
            self.document[0:2], self.document[2:5], self.document[5:8], self.document[8:12], self.document[12:14])
        return formated


class Product(models.Model):
    inactive = models.BooleanField('inativo')
    name = models.CharField('nome', max_length=255)
    bar_code = models.CharField('código de barra', max_length=30, unique=True, null=True)
    price = models.DecimalField('preço', max_digits=15, decimal_places=2)
    ncm = models.CharField('NCM', max_length=20)
    created_at = models.DateTimeField('criando em', auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('product', self.pk)

    def price_formated(self):
        return 'R$ {}'.format(number_format(self.price))
