from django.shortcuts import render
from django.views import generic
from .forms import SearchForm
from .models import Employee

class IndexView (generic.ListView):
  model = Employee

# def get_context_data(self):
#   """テンプレートを渡す辞書の作成"""
#   context = super().get_context_data()
#   context['form'] = SearchForm(self.request.GET)
#   return context
#
# def get_queryet(self)
#   """テンプレートえ渡す"""
#   form = SearchForm(self.request.GET)
#   form.is_valid()



# Create your views here.
