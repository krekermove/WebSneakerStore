from django.shortcuts import render
from django.views.generic import DetailView
from .models import Sneaker


class SneakerDetailView(DetailView):
    model = Sneaker
    template_name = 'sneakers/sneaker_detail.html'
