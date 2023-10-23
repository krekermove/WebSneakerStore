from django.contrib import admin
from .models import Sneaker

class SneakersAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'stock38', 'stock39', 'stock40', 'stock41', 'stock42', 'stock43', 'img1', 'img2', 'img3')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Sneaker, SneakersAdmin)

