from django.conf import settings
from django.core.cache import cache

from catalog.models.category import Category


def get_cashed_categories_list():
    """Функция для создания и кеширования списка категорий"""

    # Если кеширование включено
    if settings.CACHE_ENABLED:
        key = 'categories'  # ключ, по которому можно получить данные из кеша
        categories_list = cache.get(key)  # пробуем получить данные из кеша

        # если там по ключу key ничего нет
        if categories_list is None:
            categories_list = Category.objects.all()  # выборка категорий
            cache.set(key, categories_list)  # запись в кеш

    # если кеширование выключено
    else:
        categories_list = Category.objects.all()  # выборка категорий
    return categories_list
