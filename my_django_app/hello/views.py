from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import FormPemesanan

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')

def tentang(request):
    return render(request, 'tentang.html')


def galeri(request):
    return render(request, 'galeri.html')

def layanan(request):
    return render(request, 'layanan.html')

def harga(request):
    return render(request, 'harga.html')

def form_pemesanan(request):
    if request.method == "POST":
        form = FormPemesanan(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'konfirmasi_pemesanan.html', data)
    else:
        form = FormPemesanan()
    return render(request, 'form_pemesanan.html', {
        'form': form
    })