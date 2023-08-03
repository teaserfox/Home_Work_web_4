from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    slug = models.CharField(max_length=255, **NULLABLE, unique=True, verbose_name='Ссылка')
    body = models.TextField(verbose_name='Содержимое', **NULLABLE)
    image = models.ImageField(upload_to='blog/', verbose_name='изображение')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    publication_feature = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров', editable=False)

    def __str__(self):
        return f'{self.title}: {self.views_count}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        # ordering = 'title'
