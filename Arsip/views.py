from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here. 
 
def beranda(request):     
    jumlah_lpm= Lpm.objects.count()
    jumlah_sop= Sop.objects.count()
    jumlah_sk= Surat_Keputusan.objects.count()
    jumlah_PD= Pedoman.objects.count()
    context = {
        'menu' : 'home',
        'page' : 'selamat datang di Aplikasi ????????????????///',        
        'jumlah_lpm': jumlah_lpm,
        'jumlah_sop': jumlah_sop,
        'jumlah_sk': jumlah_sk,
        'jumlah_PD': jumlah_PD,
    }
    return render(request, 'Arsip/beranda.html', context)

def lpm(request): 
    list_lpm = Lpm.objects.all()    
    context = {
        'menu' : 'dokumen',
        'page' : 'dokumen lpm',
        "list_lpm" : list_lpm,       
    }
    return render(request, 'Arsip/lpm.html', context)

def pedoman(request):  
    list_pedoman = Pedoman.objects.order_by('nama_arsip')       
    context = {
        'menu' : 'dokumen',
        'page' : 'dokumen pedoman', 
        "tampilpedoman" : list_pedoman,         
    }
    return render(request, 'Arsip/pedoman.html', context)

def surat_keputusan(request): 
    list_surat_keputusan = Surat_Keputusan.objects.order_by('nama_arsip') 
    context = {
        'menu' : 'dokumen',
        'page' : 'dokumen surat keputusan', 
        "tampilsurat_keputusan" : list_surat_keputusan,        
    }
    return render(request, 'Arsip/surat_keputusan.html', context)

def sop(request):
    list_sop = Sop.objects.order_by('nama_arsip')      
    context = {
        'menu' : 'dokumen',
        'page' : 'dokumen sop',  
         "tampilsop" : list_sop,       
    }
    return render(request, 'Arsip/sop.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        cocok = authenticate(request, username=username, password=password)
        if cocok is not None:
            login(request, cocok)
            return redirect('beranda')

    context = {
        "menu" : 'Halaman Login',
        "page" : 'login',
    }
    return render(request, 'Arsip/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def tambahlpm(request):    
    formdata = LpmForm()
    if request.method == 'POST':
        formdata = LpmForm(request.POST, request.FILES)
        if formdata.is_valid:
            formdata.save()
            return redirect('lpm')        
    
    context = {
        "menu" : 'tambah lpm',
        "page" : 'tambah-lpm',   
        'formdata':formdata

    }
    return render(request, 'arsip/tambahlpm.html', context)

def tambahpedoman(request):
    tambahpedoman = PedomanForm()
    if request.method == 'POST' :        
        tambahpedoman = PedomanForm(request.POST, request.FILES)
        if tambahpedoman.is_valid:
            tambahpedoman.save()
            return redirect('pedoman')
    context = {
        "menu" : 'tambah pedoman',
        "page" : 'tambah-pedoman',
        "tambahpedoman": tambahpedoman,
    }
    return render(request, 'arsip/tambahpedoman.html', context)

def tambahsurat_keputusan(request):
    tambahsurat_keputusan = Surat_KeputusanForm()
    if request.method == 'POST' :        
        tambahsurat_keputusan = Surat_KeputusanForm(request.POST, request.FILES)
        if tambahsurat_keputusan.is_valid:
            tambahsurat_keputusan.save()
            return redirect('surat_keputusan')
    context = {
        "menu" : 'tambah surat_keputusan',
        "page" : 'tambah-surat_keputusan',
        "tambahsurat_keputusan": tambahsurat_keputusan,
    }
    return render(request, 'arsip/tambahsurat_keputusan.html', context)

def tambahsop(request):
    tambahsop = SopForm()
    if request.method == 'POST' :
        #print('cetak POST:', request.POST)
        tambahsop = SopForm(request.POST, request.FILES)
        if tambahsop.is_valid:
            tambahsop.save()
            return redirect('sop')
    context = {
        "menu" : 'tambah sop',
        "page" : 'tambah-sop',
        "tambahsop": tambahsop,
    }
    return render(request, 'arsip/tambahsop.html', context)

def editlpm (request, pk):
    up_lpm= Lpm.objects.get(id=pk)
    editlpm = LpmForm(instance=up_lpm)
    if request.method == 'POST':        
        editlpm = LpmForm(request.POST, request.FILES, instance=up_lpm)
        if editlpm.is_valid:
            editlpm.save()
            return redirect('lpm')
    context = {
        "menu" : 'editlpm',
        "page" : 'Edit lpm',
        "editlpm" : editlpm,
    }
    return render(request, 'arsip/editlpm.html', context)

def editpedoman (request, pk):
    up_pedoman= Pedoman.objects.get(id=pk)
    editpedoman = PedomanForm(instance=up_pedoman)
    if request.method == 'POST':        
        editpedoman = PedomanForm(request.POST, request.FILES, instance=up_pedoman)
        if editpedoman.is_valid:
            editpedoman.save()
            return redirect('pedoman')
    context = {
        "menu" : 'editpedoman',
        "page" : 'Edit pedoman',
        "editpedoman" : editpedoman,
    }
    return render(request, 'arsip/editpedoman.html', context)

def editsop (request, pk):
    up_sop= Sop.objects.get(id=pk)
    editsop = SopForm(instance=up_sop)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        editsop = SopForm(request.POST, request.FILES, instance=up_sop)
        if editsop.is_valid:
            editsop.save()
            return redirect('sop')
    context = {
        "menu" : 'editsop',
        "page" : 'Edit sop',
        "editsop" : editsop,
    }
    return render(request, 'arsip/editsop.html', context)

def editsurat_keputusan (request, pk):
    up_surat_keputusan= Surat_Keputusan.objects.get(id=pk)
    editsurat_keputusan = Surat_KeputusanForm(instance=up_surat_keputusan)
    if request.method == 'POST':        
        editsurat_keputusan = Surat_KeputusanForm(request.POST, request.FILES, instance=up_surat_keputusan)
        if editsurat_keputusan.is_valid:
            editsurat_keputusan.save()
            return redirect('surat_keputusan')
    context = {
        "menu" : 'editsurat_keputusan',
        "page" : 'Edit surat_keputusan',
        "editsurat_keputusan" : editsurat_keputusan,
    }
    return render(request, 'arsip/editsurat_keputusan.html', context)




def hapuslpm(request, pk):
    hapuslpm = Lpm.objects.get(id=pk)
    if request.method == 'POST':
        hapuslpm.delete()
        return redirect('lpm')
    context = {
        "menu" : 'hapuslpm',
        "page" : 'Hapus hapuslpm',
        "hapuslpm" : hapuslpm,
    }
    return render(request, 'arsip/hapuslpm.html', context)

def hapuspedoman(request, pk):
    hapuspedoman = Pedoman.objects.get(id=pk)
    if request.method == 'POST':
        hapuspedoman.delete()
        return redirect('pedoman')
    context = {
        "menu" : 'hapuspedoman',
        "page" : 'Hapus hapuspedoman',
        "hapuspedoman" : hapuspedoman,
    }
    return render(request, 'arsip/hapuspedoman.html', context)

def hapussop(request, pk):
    hapussop = Sop.objects.get(id=pk)
    if request.method == 'POST':
        hapussop.delete()
        return redirect('sop')
    context = {
        "menu" : 'hapussop',
        "page" : 'Hapus hapussop',
        "hapussop" : hapussop,
    }
    return render(request, 'arsip/hapussop.html', context)

def hapussurat_keputusan(request, pk):
    hapussurat_keputusan = Surat_Keputusan.objects.get(id=pk)
    if request.method == 'POST':
        hapussurat_keputusan.delete()
        return redirect('surat_keputusan')
    context = {
        "menu" : 'hapussurat_keputusan',
        "page" : 'Hapus hapussurat_keputusan',
        "hapussurat_keputusan" : hapussurat_keputusan,
    }
    return render(request, 'arsip/hapussurat_keputusan.html', context)


def cetak_LPM(request): 
    if 'chek' in request.GET:
        cetak=request.GET['chek']
        list_lpm = Lpm.objects.filter(id=cetak)
    else:
        list_lpm = Lpm.objects.filter(id=None)               

    context = {        
        "list_lpm" : list_lpm,       
    }
    return render(request, 'Arsip/Laporan/lp_LPM.html', context)

def cetak_SOP(request): 
    if 'chek' in request.GET:
        cetak=request.GET['chek']
        data = Sop.objects.filter(id=cetak)
    else:
        data = Sop.objects.filter(id=None)               

    context = {        
        "data" : data,       
    }
    return render(request, 'Arsip/Laporan/lp_sop.html', context)

def cetak_SK(request): 
    if 'chek' in request.GET:
        cetak=request.GET['chek']
        data = Surat_Keputusan.objects.filter(id=cetak)
    else:
        data = Surat_Keputusan.objects.filter(id=None)               

    context = {        
        "data" : data,       
    }
    return render(request, 'Arsip/Laporan/lp_sk.html', context)

def cetak_Pedoman(request): 
    if 'chek' in request.GET:
        cetak=request.GET['chek']
        data = Pedoman.objects.filter(id=cetak)
    else:
        data = Pedoman.objects.filter(id=None)               

    context = {        
        "data" : data,       
    }
    return render(request, 'Arsip/Laporan/lp_pedoman.html', context)


#petugas
def petugasdata(request): 
    data = User.objects.all()    
    context = {        
        "data" : data,       
    }
    return render(request, 'Arsip/data_user/tabel.html', context)

def T_petugasdata(request): 
    formdata = UserCreationForm()
    if request.method == 'POST':
        formdata = UserCreationForm(request.POST)
        if formdata.is_valid:
            formdata.save()
            return redirect('petugas')        
    

    context = {        
        "formdata" : formdata,       
    }
    return render(request, 'Arsip/data_user/input.html', context)

def editpetugas (request, id):
    edit_petugas= User.objects.get(id=id)
    edit = UserCreationForm(instance=edit_petugas)
    if request.method == 'POST':        
        edit = UserCreationForm(request.POST, instance=edit_petugas)
        if edit.is_valid:
            edit.save()
            return redirect('petugas')
    context = {        
        "edit" : edit,
    }
    return render(request, 'Arsip/data_user/edit.html', context)

def hapusPetugas(request, id_p):
    User.objects.filter(id=id_p).delete()
    return redirect('petugas')   


#menu laporan
def menu_laporandata(request):     
    context = {
        'menu' : 'menu laporan',        
    }
    return render(request, 'Arsip/Laporan_ALL/menu_laporan.html', context)

def lp_LPM(request): 
    list_lpm = Lpm.objects.all()    
    context = {        
        "list_lpm" : list_lpm,       
    }
    return render(request, 'Arsip/Laporan_ALL/lp_LPM.html', context)

def lp_SOP(request): 
    data = Sop.objects.all()    
    context = {        
        "data" : data,       
    }
    return render(request, 'Arsip/Laporan_ALL/lp_sop.html', context)    

def lp_SK(request): 
    data = Surat_Keputusan.objects.all()    
    context = {        
        "data" : data,       
    }
    return render(request, 'Arsip/Laporan_ALL/lp_sk.html', context)    

def lp_PD(request): 
    data = Pedoman.objects.all()    
    context = {        
        "data" : data,       
    }
    return render(request, 'Arsip/Laporan_ALL/lp_pedoman.html', context)    