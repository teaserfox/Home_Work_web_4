from django.urls import path, include
import catalog
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import contacts, HomeListView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', HomeListView.as_view(), name='home'),

]