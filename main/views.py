import datetime
from django.shortcuts import render, redirect
from .forms import OfferForm
import sys
sys.path.append("..")
from sneakers.models import Sneaker


def index(request):
	sneakers = Sneaker.objects.all()
	return render(request, 'main/index.html', {'sneakers': sneakers})

def cart(request):
	sneakers = Sneaker.objects.all()
	total = 0
	if request.session.get('cart'):
		for item in request.session['cart']:
			total += int(item['cost'])
	return render(request, 'main/cart.html', {'sneakers': sneakers, 'total': total})

def offer(request):
	sneakers = Sneaker.objects.all()
	total = 0
	error = ''
	if request.method == 'POST':
		form = OfferForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.region = form.cleaned_data.get('region')
			instance.city = form.cleaned_data.get('city')
			instance.street = form.cleaned_data.get('street')
			instance.house = form.cleaned_data.get('house')
			instance.mobile = form.cleaned_data.get('mobile')
			instance.date = datetime.date.today()
			sneakers_list = []
			for sneaker in sneakers:
				for item in request.session['cart']:
					if int(sneaker.id) == int(item['id']):
						obj = Sneaker.objects.get(id=sneaker.id)
						sneakers_data = {
							'name': obj.name,
							'size': item['size'],
						}
						sneakers_list.append(sneakers_data)
			instance.sneakers = sneakers_list
			instance.save()
			return redirect('home')
		else:
			error = 'Форма заполнена неправильно'

	if request.session.get('cart'):
		for item in request.session['cart']:
			total += int(item['cost'])
	form = OfferForm()

	data = {
		'form': form,
		'error': error,
		'total': total,
		'sneakers': sneakers,
	}
	return render(request, 'main/offer.html', data)
