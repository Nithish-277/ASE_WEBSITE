from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('home/',views.home,name = 'home'),
    path('forum/',views.forum,name = 'forums'),
    # path('remainders',views.remainder,name = 'remainder'),
    path('upload/',views.uploads,name="Upload"),
    path('prescriptionsearch/',views.searchprescription,name="searchprescription"),
    path('reportsearch/',views.searchreport,name="searchreport"),
    path('files/',views.temporary_files,name="Files"),
    path('files/media/files/prescriptions/<int:pk>/', views.delete_prescription, name='delete_prescription'),
    path('files/media/files/reports/<int:pk>/', views.delete_report, name='delete_report'),
    path('editprescription/<int:pk>/',views.edit_prescription, name='edit_prescription'),
    path('editreport/<int:pk>/',views.edit_report, name='edit_report'),
    path('posts/',include('forum.urls')),
    path('profile/',include('forum.urls')),
    path('remainder/',include('notifications.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
