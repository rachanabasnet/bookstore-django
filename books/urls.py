from django.conf.urls.static import static
from django.urls import path

from bookstore import settings
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('books/', views.books, name='books'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)