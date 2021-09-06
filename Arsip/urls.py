from django.urls import path 
from Aplikasi import settings
from django.conf.urls.static import static  
from . import views
urlpatterns = [     
    path('beranda/', views.beranda, name='beranda'),  
    path('login/', views.login, name='login'),  
    path('lpm/', views.lpm, name='lpm'),  
    path('sop/', views.sop, name='sop'),  
    path('surat_keputusan/', views.surat_keputusan, name='surat_keputusan'), 
    path('pedoman/', views.pedoman, name='pedoman'), 
    path('tambahlpm/', views.tambahlpm, name='tambahlpm'), 
    path('tambahpedoman/', views.tambahpedoman, name='tambahpedoman'), 
    path('tambahsurat_keputusan/', views.tambahsurat_keputusan, name='tambahsurat_keputusan'),
    path('tambahsop/', views.tambahsop, name='tambahsop'),
    path('editlpm/<str:pk>', views.editlpm, name='editlpm'),
    path('editpedoman/<str:pk>', views.editpedoman, name='editpedoman'),
    path('editsop/<str:pk>', views.editsop, name='editsop'),
    path('editsurat_keputusan/<str:pk>', views.editsurat_keputusan, name='editsurat_keputusan'),
    path('hapuslpm/<str:pk>', views.hapuslpm, name='hapuslpm'),
    path('hapuspedoman/<str:pk>', views.hapuspedoman, name='hapuspedoman'),
    path('hapussop/<str:pk>', views.hapussop, name='hapussop'),
    path('hapussurat_keputusan/<str:pk>', views.hapussurat_keputusan, name='hapussurat_keputusan'),
   
   #laporan
   path('lp_pm/', views.cetak_LPM, name='lp_pm'), 
   path('lp_sop/', views.cetak_SOP, name='lp_sop'), 
   path('lp_sk/', views.cetak_SK, name='lp_sk'), 
   path('lp_pedoman/', views.cetak_Pedoman, name='lp_pedoman'), 

   #petugas
   path('petugas/', views.petugasdata, name='petugas'), 
   path('t_petugas/', views.T_petugasdata, name='t_petugas'), 
   path('edit_petugas/<str:id>', views.editpetugas, name='edit_petugas'),
   path('hapus_petugas/<str:id_p>', views.hapusPetugas, name='hapus_petugas'),


   #menu laporan
   path('Menu_LP/', views.menu_laporandata, name='Menu_LP'), 
   path('LP_PM/', views.lp_LPM, name='LP_PM'), 
   path('LP_SOP/', views.lp_SOP, name='LP_SOP'), 
   path('LP_SK/', views.lp_SK, name='LP_SK'), 
   path('LP_PD/', views.lp_PD, name='LP_PD'), 
] 
if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)