from django.core.management import BaseCommand

from catalog.models.category import Category
from catalog.models.products import Product


class Products:
    pass


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Список категорий для добавления
        categories = [
            {'name': 'Классическая зарубежная проза'},
            {'name': 'Исторический детектив'},
            {'name': 'Классическая отечественная проза'},
            {'name': 'Личная эффективность, мотивация'}
        ]

        # Очистка таблицы Category
        Category.objects.all().delete()

        # Список экземпляров класса Category
        categories_for_create = []
        for category in categories:
            categories_for_create.append(Category(**category))

        # Добавление категорий в базу данных
        Category.objects.bulk_create(categories_for_create)

        # Список продуктов для добавления в БД
        products = [{'name': 'Повелитель мух',
                     'purchase_price': 276,
                     'category': categories_for_create[0],  # Классическая зарубежная проза
                     'description': 'Если лицо совершенно меняется от того, сверху или снизу его осветить, '
                                    '— чего же стоит лицо? И чего же всё '
                                    'вообще тогда стоит?'},

                    {'name': 'Десять негритят',
                     'purchase_price': 299,
                     'category': categories_for_create[1],  # Исторический детектив
                     'description': 'У сумасшедшего уйма преимуществ перед нормальными людьми. Они вдвое хитрее.'},


                    {'name': 'Идиот',
                     'purchase_price': 329,
                     'category': categories_for_create[2],  # Классическая отечественная проза
                     'description': 'Я пришел вас предупредить: во-первых, мне денег взаймы не давать, '
                     'потому что я непременно буду просить.'},

                    {'name': '48 законов',
                     'purchase_price': 479,
                     'category': categories_for_create[3],  # Личная эффективность, мотивация
                     'description': 'Мудрец получит больше пользы от своих врагов, чем глупец от своих друзей.'}
                    ]

        # Очистка таблицы Product
        Product.objects.all().delete()

        # Список экземпляров класса Product
        products_for_create = []
        for product in products:
            products_for_create.append(Product(**product))

        # Добавление продуктов в базу данных
        Product.objects.bulk_create(products_for_create)
