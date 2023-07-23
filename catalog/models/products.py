from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название продукта')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='изображение')
    category = models.ForeignKey('catalog.Category', on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    purchase_price = models.IntegerField(verbose_name='Цена')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.purchase_price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)
