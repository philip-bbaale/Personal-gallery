from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('', views.pictures_index, name='pictures_index'),
    url(r'^search/', views.search_results, name='search_results'),
    path('<int:pk>/', views.pictures_detail, name='pictures_detail'),
    path('<category>/', views.pictures_category, name="pictures_category"),
    path('<location>/', views.pictures_location, name="pictures_location"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)