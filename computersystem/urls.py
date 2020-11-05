from . import views 
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from computersystem.views import computers,computer_entry,index


urlpatterns = [
    
    path('', views.index, name='index'),
    path('computers', views.computers, name='computers'),
    path('computer_entry', views.computer_entry, name='computer_entry'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
