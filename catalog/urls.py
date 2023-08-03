from django.urls import path, include
import catalog
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import contacts, HomeListView, HomeCreateView, HomeUpdateView

app_name = CatalogConfig.name


urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', HomeListView.as_view(), name='home'),
    path('create/', HomeCreateView.as_view(), name='create_home'),
    path('update/<int:pk>/', HomeUpdateView.as_view(), name='update_home'),

]
