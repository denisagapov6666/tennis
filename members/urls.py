from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name = 'main'),
    path('members/',views.members, name = 'members'),
    path('members/details/<slug:slug>',views.details, name= "details"),
    path('testing', views.testing, name= 'testing'),
    path("fileuploads",views.upload_file_init,name = 'fileuploads')
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)