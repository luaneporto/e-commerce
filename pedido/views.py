from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse

class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')


class Fechar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Fechar')


class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')
