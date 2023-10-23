from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
	path('<id>/add/', views.add_to_cart, name='add_to_cart'),
	path('<id>/remove/', views.remove_from_cart, name='remove_from_cart'),
	path('<id>/remove/', views.remove_from_cart, name='remove_from_cart'),
	path('delete/', views.delete, name='delete'),
]
