from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm
from catalog.models.products import Product
from django.urls import reverse_lazy, reverse


# Create your views here.


def contacts(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name} \nТелефон {phone} \nСообщение {message}')

    return render(request, 'catalog/contacts.html')


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


# def home(request):
#     products_list = Product.objects.all()
#     context = {'object_list': products_list}
#     return render(request, 'catalog/home.html', context)

class HomeCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class HomeUpdateView(UpdateView):
    pass
