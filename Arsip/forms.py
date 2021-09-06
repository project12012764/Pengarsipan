from django import forms
from django.forms import ModelForm
from .models import *
class LpmForm(forms.ModelForm):
    class Meta:
        model = Lpm
        fields = ['nama_arsip', 'dokumen', 'kategori', 'bulan', 'tanggal', 'tanggal_sah']


class PedomanForm(ModelForm):
    class Meta:
        model = Pedoman
        fields = ['nama_arsip', 'dokumen','kategori','bulan', 'tanggal',  'tanggal_sah']


class Surat_KeputusanForm(ModelForm):
    class Meta:
        model = Surat_Keputusan
        fields = ['nama_arsip', 'dokumen', 'kategori', 'bulan', 'tanggal', 'tanggal_sah']


class SopForm(ModelForm):
    class Meta:
        model = Sop
        fields = ['nama_arsip', 'dokumen', 'kategori', 'bulan', 'tanggal', 'tanggal_sah']

class PetugasForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

            
           
