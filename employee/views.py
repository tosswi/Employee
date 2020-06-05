from django.shortcuts import render
from django.views import generic
from .forms import SearchForm
from .models import Employee

class IndexView (generic.ListView):
  model = Employee
  paginate_by = 1

  def get_context_data(self):
    """テンプレートを渡す辞書の作成"""
    context = super().get_context_data()
    context['form'] = SearchForm(self.request.GET)
    return context

  def get_queryset(self):
    """テンプレートえ渡す"""
    form = SearchForm(self.request.GET)
    form.is_valid()
    queryset = super().get_queryset()
    department =form.cleaned_data['department']
    if department:
      queryset=queryset.filter(department = department)

    club = form.cleaned_data['club']
    if club:
      queryset=queryset.filter(club = club)
    return queryset


# Create your views here.
