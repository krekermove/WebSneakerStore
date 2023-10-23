from django.urls import path
from . import views
from .views import SneakerDetailView



urlpatterns = [
	path('<slug:slug>', SneakerDetailView.as_view(), name='sneaker_detail'),
]
