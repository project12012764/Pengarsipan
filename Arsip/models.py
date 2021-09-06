from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lpm(models.Model):
    bulan = (
        ('januari', 'januari'),
        ('februari', 'februari'),
        ('maret', 'maret'),
        ('april', 'april'),
        ('mei', 'mei'),
        ('juni', 'juni'),
        ('juli', 'juli'),
        ('agustus', 'agustus'),
        ('september', 'september'),
        ('oktober', 'oktober'),
        ('november', 'november'),
        ('desember', 'desember'),

    )
    kategori = (
        ('UNUJA','UNUJA'),
        ('FAKULTAS','FAKULTAS'),
        ('LEMBAGA','LEMBAGA'),
    )
    nama_arsip = models.CharField(max_length=100, blank=True, null=True,)
    dokumen = models.FileField(upload_to='documents/', null=True)
    kategori = models.CharField(max_length=20, blank=True, null=True, choices=kategori)
    bulan = models.CharField(max_length=20, blank=True, null=True, choices=bulan)
    tanggal = models.CharField(max_length=100, blank=True, null=True,)
    tanggal_sah = models.CharField(max_length=100, blank=True, null=True,)

    def __str__(self):
        return '%s' % (self.nama_arsip)
    class Meta:
        verbose_name_plural ="Lpm"

class Pedoman(models.Model):
    bulan = (
        ('januari', 'januari'),
        ('februari', 'februari'),
        ('maret', 'maret'),
        ('april', 'april'),
        ('mei', 'mei'),
        ('juni', 'juni'),
        ('juli', 'juli'),
        ('agustus', 'agustus'),
        ('september', 'september'),
        ('oktober', 'oktober'),
        ('november', 'november'),
        ('desember', 'desember'),

    )
    kategori = (
        ('UNUJA','UNUJA'),
        ('FAKULTAS','FAKULTAS'),
        ('LEMBAGA','LEMBAGA'),
    )
   
    nama_arsip = models.CharField(max_length=100, blank=True, null=True,)
    dokumen = models.FileField(upload_to='documents/', null=True)
    kategori = models.CharField(max_length=20, blank=True, null=True, choices=kategori)
    bulan = models.CharField(max_length=20, blank=True, null=True, choices=bulan)
    tanggal = models.CharField(max_length=100, blank=True, null=True,)
    tanggal_sah = models.CharField(max_length=100, blank=True, null=True,)

   


    def __str__(self):
        return '%s' % (self.nama_arsip)
    class Meta:
        verbose_name_plural ="Pedoman"

class Surat_Keputusan(models.Model):
    bulan = (
        ('januari', 'januari'),
        ('februari', 'februari'),
        ('maret', 'maret'),
        ('april', 'april'),
        ('mei', 'mei'),
        ('juni', 'juni'),
        ('juli', 'juli'),
        ('agustus', 'agustus'),
        ('september', 'september'),
        ('oktober', 'oktober'),
        ('november', 'november'),
        ('desember', 'desember'),

    )
    kategori = (
        ('UNUJA','UNUJA'),
        ('FAKULTAS','FAKULTAS'),
        ('LEMBAGA','LEMBAGA'),
        )
    
    nama_arsip = models.CharField(max_length=100, blank=True, null=True,)
    dokumen = models.FileField(upload_to='documents/', null=True) 
    kategori = models.CharField(max_length=20, blank=True, null=True, choices=kategori)   
    bulan = models.CharField(max_length=20, blank=True, null=True, choices=bulan)
    tanggal = models.CharField(max_length=100, blank=True, null=True,)
    tanggal_sah = models.CharField(max_length=100, blank=True, null=True,)
    


    def __str__(self):
        return '%s' % (self.nama_arsip)
    class Meta:
        verbose_name_plural ="Surat_Keputusan"

class Sop(models.Model):
    bulan = (
        ('januari', 'januari'),
        ('februari', 'februari'),
        ('maret', 'maret'),
        ('april', 'april'),
        ('mei', 'mei'),
        ('juni', 'juni'),
        ('juli', 'juli'),
        ('agustus', 'agustus'),
        ('september', 'september'),
        ('oktober', 'oktober'),
        ('november', 'november'),
        ('desember', 'desember'),

    )
    kategori = (
        ('UNUJA','UNUJA'),
        ('FAKULTAS','FAKULTAS'),
        ('LEMBAGA','LEMBAGA'),
        )
    nama_arsip = models.CharField(max_length=100, blank=True, null=True,)
    dokumen = models.FileField(upload_to='documents/', null=True)
    kategori = models.CharField(max_length=20, blank=True, null=True, choices=kategori) 
    bulan = models.CharField(max_length=20, blank=True, null=True, choices=bulan)
    tanggal = models.CharField(max_length=100, blank=True, null=True,)
    tanggal_sah = models.CharField(max_length=100, blank=True, null=True,)

    def __str__(self):
        return '%s' % (self.nama_arsip)
    class Meta:
        verbose_name_plural ="Sop"