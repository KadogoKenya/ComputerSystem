from . import views 
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from computersystem.views import computers,computer_entry,index,computer_list,operating_system


urlpatterns = [
    
    path('', views.index, name='index'),
    path('computers', views.computers, name='computers'),
    path('computer_entry', views.computer_entry, name='computer_entry'),
    path('computer_list', views.computer_list, name='computer_list'),
    url(r'^computers/(?P<id>\d+)/$', views.computer_edit, name='computer_edit'),
    url(r'^computers/(?P<id>\d+)/delete$', views.computer_delete, name='computer_delete'),
    path('operating_system', views.operating_system, name='operating_system'),


# r'^(?P<album_id>[0-9])/$'

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
