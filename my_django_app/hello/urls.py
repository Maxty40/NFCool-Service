from django.urls import path, include
<<<<<<< HEAD

=======
>>>>>>> 81e4409 (Update Form)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    path('salam/', views.salam, name='salam'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
=======
    path('home/', views.home, name='home'),
    path('layanan/', views.layanan, name='layanan'),
    path('harga/', views.harga, name='harga'),
    path('tentang/', views.tentang, name='tentang'),
    path('galeri/', views.galeri, name='galeri'),
>>>>>>> 81e4409 (Update Form)
    path('form_pemesanan/', views.form_pemesanan, name='form_pemesanan'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]
