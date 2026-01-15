from django import forms
from django.core.exceptions import ValidationError
from datetime import date

class FormPemesanan(forms.Form):
    nama = forms.CharField( 
        max_length = 100,
        label = "Nama Lengkap",
        widget = forms.TextInput(attrs={
            'class': 'form-control'
            })
    )
    email = forms.EmailField(
        widget = forms.EmailInput(attrs={
            'class': 'form-control'
        })
    )
    telepon = forms.CharField(
        max_length = 15,
        widget = forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    jenis_layanan = forms.ChoiceField(
        choices = [
            ('', 'Pilih Jenis Layanan'),
            ('Pemasangan AC Baru', 'Pemasangan AC Baru'),
            ('Servis AC', 'Servis AC'),
            ('Perbaikan AC', 'Perbaikan AC'),
            ],
        widget = forms.Select(attrs={
            'class': 'form-select'
        })
    )
    
    alamat = forms.CharField(
        widget = forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3
        })
    )
    tanggal = forms.DateField(
        widget = forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }),
        label = "Tanggal Layanan"
    )
    merk_model = forms.CharField(
        required = True,
        widget = forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    waktu = forms.ChoiceField(
        choices = [
            ('', 'Pilih Waktu Layanan'),
            ('Pagi', 'Pagi (08:00 - 12:00)'),
            ('Siang', 'Siang (12:00 - 16:00)'),
            ('Sore', 'Sore (16:00 - 20:00)'),
        ],
        widget = forms.Select(attrs={
            'class': 'form-select'
        })
    )
    detail_tambahan = forms.CharField(
        required = False,
        widget = forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3
        })
    )
    
    def clean_telepon(self):
        telepon = self.cleaned_data['telepon']
        if not telepon.isdigit():
            raise ValidationError("Nomor telepon hanya boleh angka!")
        if len(telepon) < 10:
            raise ValidationError("Nomor telepon minimal 10 digit!")
        return telepon
    
    def clean_tanggal(self):
        tanggal = self.cleaned_data['tanggal']
        if tanggal < date.today():
            raise ValidationError("Tanggal tidak boleh di masa lalu!")
        return tanggal