from django.urls import path, include
import catalog
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import contacts, HomeListView, HomeCreateView, HomeUpdateView, VersionListView, HomeDeleteView

app_name = CatalogConfig.name


urlpatterns = [
    path('contacts/', contacts, name='contacts'),  # http://127.0.0.1:8000/contacts/  Контакты
    path('', HomeListView.as_view(), name='home'),  # http://127.0.0.1:8000/ Главная страница
    # path('create/', HomeCreateView.as_view(), name='create_home'),
    # path('update/<int:pk>/', HomeUpdateView.as_view(), name='update_home'),
    path('create/', HomeCreateView.as_view(), name='create_home'),  # http://127.0.0.1:8000/create/
    path('update/<int:pk>/', HomeUpdateView.as_view(), name='update_home'),  # http://127.0.0.1:8000/create/<pk>
    path('delete/<int:pk>/', HomeDeleteView.as_view(), name='delete_home'),  # http://127.0.0.1:8000/delete/<pk>
    path('versions/<int:pk>', VersionListView.as_view(), name='version'),  # http://127.0.0.1:8000/versions/<pk>

]
