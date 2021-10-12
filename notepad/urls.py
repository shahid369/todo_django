from os import stat
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from notes.views import note_list_view,finished_item,delete_item,recover_item
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',note_list_view,name='note-list'),
    path('finished-item/<id>/',finished_item,name='finished-note-item'),
    path('delete-item/<id>/',delete_item,name='delete-note-item'),
    path('recover_item/<id>/',recover_item,name='recover-note-item'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)