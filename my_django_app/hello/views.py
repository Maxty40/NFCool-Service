from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
<<<<<<< HEAD


def salam(request):
    return HttpResponse("<h1 align='center'>Selamat Belajar Django</h1>")


=======
>>>>>>> 81e4409 (Update Form)
def home(request):
    return render(request, 'home.html')


<<<<<<< HEAD
def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')

def form_pemesanan(request):
=======
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
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        telepon = request.POST.get('telepon')
        jenis_layanan = request.POST.get('jenis_layanan')
        tanggal = request.POST.get('tanggal')
        alamat = request.POST.get('alamat')
        merek_model = request.POST.get('merek_model')
        waktu = request.POST.get('waktu')
        detail_tambahan = request.POST.get('detail_tambahan')
        data = {
            'nama': nama,
            'email': email,
            'telepon': telepon,
            'jenis_layanan': jenis_layanan,
            'tanggal': tanggal,
            'alamat': alamat,
            'merek_model': merek_model,
            'waktu': waktu,
            'detail_tambahan': detail_tambahan
        }
        return render(request, 'konfirmasi_pemesanan.html', data)
>>>>>>> 81e4409 (Update Form)
    return render(request, 'form_pemesanan.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            return redirect('login')

    return render(request, 'signup.html')
