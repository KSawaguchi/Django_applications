from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import VideoCreateForm
from .models import Video
# Create your views here.

class IndexView(generic.ListView):
    model = Video


class CreateView(generic.CreateView):
    model = Video
    form_class = VideoCreateForm
    success_url = reverse_lazy('tube:index')


class PlayView(generic.DetailView):
    model = Video