from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms import inlineformset_factory
from catalog.forms import ProductForm, VersionForm
from catalog.models.products import Product
from django.urls import reverse_lazy, reverse

from catalog.models.version import Version
from catalog.services import get_cashed_categories_list


# Create your views here.


def contacts(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name} \nТелефон {phone} \nСообщение {message}')

    return render(request, 'catalog/contacts.html')


def categories_list(request):
    categories = get_cashed_categories_list()
    context = {'object_list': categories, }
    return render(request, 'catalog/categories.html', context)


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

# def home(request):
#     products_list = Product.objects.all()
#     context = {'object_list': products_list}
#     return render(request, 'catalog/home.html', context)


class HomeCreateView(CreateView):
    """Класс-контроллер для создания продукта"""
    model = Product  # Модель, с которой он работает
    form_class = ProductForm  # Форма для заполнения
    success_url = reverse_lazy('catalog:home')


class HomeUpdateView(UpdateView):
    """
    Класс-контроллер для редактирования продукта
    """
    model = Product  # Модель, с которой он работает
    form_class = ProductForm  # Форма для заполнения
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        """
        Переопределение метода get_context_data, добавление в контекст формсета
        """
        context_data = super().get_context_data(**kwargs)
        # 1-Родительская модель 2-модель версия 3-модель формы extra-количество новых форм
        VersionFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        """В случае успешного заполнения формы перенаправление на страницу с версиями соответствующего продукта
        """
        return reverse('catalog:version', args=[self.kwargs.get('pk')])


class HomeDeleteView(DeleteView):
    """Класс-контроллер для удаления продукта"""
    model = Product  # Модель, с которой он работает
    # URL адрес, на который происходит перенаправление после успешного удаления записи в блоге
    success_url = reverse_lazy('catalog:home')


class VersionListView(ListView):
    """
    Класс-контроллер для отображения списка активных версии текущего продукта
    """
    model = Version

    def get_queryset(self, *args, **kwargs):
        """
        Переопределение метода get_queryset для возможности отфильтровать активные версии продукта с нужным id
        """
        product_pk = self.kwargs.get('pk')  # получение id продукта
        return Version.objects.filter(is_active=True, product_id=product_pk)

    def get_context_data(self, *args, object_list=None, **kwargs):
        """
        Переопределение метода get_context_data для передачи в шаблон и отображения на странице
         наименования продукта
         """
        product = Product.objects.get(pk=self.kwargs.get('pk'))  # Получение продукта с соответствующим id
        context = super().get_context_data(*args, **kwargs)  # получение контекста
        context['product_name'] = product.name  # добавление в контекст наименования продукта
        context['pk'] = product.pk  # добавление в контекст id продукта
        return context
