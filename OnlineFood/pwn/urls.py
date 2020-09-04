from django.conf.urls.static import static
from django.urls import path

from OnlineFood import settings
from pwn import views

urlpatterns = [

    path('',views.showIndex,name='pwn_main'),
    path('pwn_login_check/',views.pwn_login_check,name='pwn_login_check'),
    path('welcome/',views.welcome,name='welcome'),
    path('state/',views.openState,name='state'),
    path('city/',views.openCity,name='city'),
    path('cuisine/',views.openCusine,name='cuisine'),
    path('vendor/',views.openVendor,name='vendor'),
    path('resports/',views.openReporsts,name='reports'),
    path('logout/',views.pwn_login_check,name='logout'),
    path('savestate/',views.savestate,name='savestate'),
    path('updatestate/',views.updatestate,name='updatestate'),
    path('updatestateid/',views.updatestateid,name='updatestateid'),
    path('sdelete/',views.sdelete,name='sdelete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)