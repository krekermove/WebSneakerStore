from django.contrib import admin
from .models import Offer

class OfferAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile', 'sneakers', 'date', 'region', 'city', 'street', 'house')

admin.site.register(Offer, OfferAdmin)

