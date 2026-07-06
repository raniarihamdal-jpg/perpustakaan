from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('adminku/', views.admin),
    path('buku/', views.buku),
    path('anggota/', views.anggota),
    path('petugas/', views.petugas),
    path('transaksi/', views.transaksi),
    path('notifikasi/', views.notifikasi),
    path('laporan/', views.laporan),
]