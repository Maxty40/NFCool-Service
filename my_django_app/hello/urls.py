from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('layanan/', views.layanan, name='layanan'),
    path('harga/', views.harga, name='harga'),
    path('tentang/', views.tentang, name='tentang'),
    path('galeri/', views.galeri, name='galeri'),
    path('form_pemesanan/', views.form_pemesanan, name='form_pemesanan'),
]
