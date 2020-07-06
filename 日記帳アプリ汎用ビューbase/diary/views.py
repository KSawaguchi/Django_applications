from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreateForm
from .models import Day
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
class IndexView(generic.ListView):
    model = Day
    paginate_by = 3

class AddView(LoginRequiredMixin, generic.CreateView):
    model = Day
    form_class = DayCreateForm #fields = '__all__'でformを作らなくても可
    success_url = reverse_lazy('diary:index')

class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Day
    form_class = DayCreateForm #fields = '__all__'でformを作らなくても可
    success_url = reverse_lazy('diary:index')

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Day
    success_url = reverse_lazy('diary:index')

class DetailView(generic.DetailView):
    model = Day
