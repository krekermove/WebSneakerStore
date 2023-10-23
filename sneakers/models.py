from django.db import models
from django.urls import reverse
import sys, os
sys.path.append(os.path.abspath('../accounts.models'))
from accounts.models import User

class Sneaker(models.Model):
    name = models.CharField('Название', max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(null=False, unique=False)
    img1 = models.ImageField(default=None, upload_to='files/cover/')
    img2 = models.ImageField(default=None, upload_to='files/cover/')
    img3 = models.ImageField(default=None, upload_to='files/cover/')
    stock38 = models.DecimalField(max_digits=10, decimal_places=2)
    stock39 = models.DecimalField(max_digits=10, decimal_places=2)
    stock40 = models.DecimalField(max_digits=10, decimal_places=2)
    stock41 = models.DecimalField(max_digits=10, decimal_places=2)
    stock42 = models.DecimalField(max_digits=10, decimal_places=2)
    stock43 = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sneaker_detail', args=[str(self.slug)])


    class Meta:
        verbose_name = 'Кроссовки'
        verbose_name_plural = 'Кроссовки'