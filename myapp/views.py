from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def admin(request):
    return render(request, 'adminku.html')

def buku(request):
    return render(request, 'buku.html')

def anggota(request):
    return render(request, 'anggota.html')

def petugas(request):
    return render(request, 'petugas.html')

def transaksi(request):
    return render(request, 'transaksi.html')

def notifikasi(request):
    return render(request, 'notifikasi.html')

def laporan(request):
    return render(request, 'laporan.html')
