from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', views.index, name='home'),
	path('cart', views.cart, name='cart'),
	path('offer', views.offer, name='offer'),
]
