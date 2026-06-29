from django.contrib import admin

# Register your models here.
from .models import (
    Admin,
    Kategori,
    Buku,
    Mahasiswa,
    Petugas,
    Peminjaman,
    Notifikasi,
    Laporan,
    Pengembalian,
    Denda)

admin.site.register(Admin)
admin.site.register(Kategori)
admin.site.register(Buku)
admin.site.register(Mahasiswa)
admin.site.register(Petugas)
admin.site.register(Peminjaman)
admin.site.register(Notifikasi)
admin.site.register(Laporan)
admin.site.register(Pengembalian)
admin.site.register(Denda)
