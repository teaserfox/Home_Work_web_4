from django.db import models

from catalog.models.products import Product

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='название книги')
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=350, verbose_name='название версии')

    active_version = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product} - {self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
