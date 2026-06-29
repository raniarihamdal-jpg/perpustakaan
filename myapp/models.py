from django.db import models

# Create your models here.
class Admin(models.Model):
    nama = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=10)

class Kategori(models.Model):
    namakategori = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=100)

class Buku(models.Model):
    judul = models.CharField(max_length=50)
    penulis = models.CharField(max_length=50)
    penerbit = models.CharField(max_length=50)
    tahunterbit = models.IntegerField()
    isbn = models.CharField(max_length=13)
    statusBuku = models.CharField(max_length=10)
    kategori_id = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE)

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    programstudi = models.CharField(max_length=50)
    angkatan = models.IntegerField()

class Petugas(models.Model):
    nama = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=10)

class Peminjaman(models.Model):
    tanggalPinjam = models.DateField()
    tanggalJatuhTempo = models.DateField()
    jumlahPerpanjangan = models.IntegerField()
    statusPinjam = models.CharField(max_length=10)
    nim = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    buku_id = models.ForeignKey(Buku, on_delete=models.CASCADE)
    petugas_id = models.ForeignKey(Petugas, on_delete=models.CASCADE)

class Notifikasi(models.Model):
    pesan = models.CharField(max_length=200)
    tanggalKirim = models.DateField()
    statusBaca = models.CharField(max_length=20)
    nim = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)

class Laporan(models.Model):
    jenisLaporan = models.CharField(max_length=50)
    tanggalCetak = models.DateField()
    petugas_id = models.ForeignKey(Petugas, on_delete=models.CASCADE)

class Pengembalian(models.Model):
    tanggalPengembalian = models.DateField()
    kondisiBuku = models.CharField(max_length=20)
    statusPengembalian = models.CharField(max_length=20)
    pinjam_id = models.CharField(max_length=30)
    petugas_id = models.ForeignKey(Petugas, on_delete=models.CASCADE)

class Denda(models.Model):
    jumlahDenda = models.DecimalField(max_digits=10, decimal_places=2)
    alasanDenda = models.CharField(max_length=100)
    statusBayar = models.CharField(max_length=20)
    kembali = models.CharField(max_length=30)
    

