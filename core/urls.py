from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from core.settings import ENVIRONMENT, MEDIA_ROOT, STATIC_ROOT
from src.core.handlers import (
    handler404, handler500
)

urlpatterns = []

""" HANDLERS ------------------------------------------------------------------------------------------------------- """
handler404 = handler404
handler500 = handler500

""" INTERNAL REQUIRED APPS ----------------------------------------------------------------------------------------- """
urlpatterns += [
    path('', include('src.web.urls')),
    path('', include('src.services.events.urls', namespace='events')),
    path('', include('src.services.departments.urls', namespace='departments')),
]

""" EXTERNAL REQUIRED APPS ----------------------------------------------------------------------------------------- """
urlpatterns += [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]

""" STATIC AND MEDIA FILES ----------------------------------------------------------------------------------------- """
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
]

""" DEVELOPMENT ONLY -------------------------------------------------------------------------------------------- """
if ENVIRONMENT != 'server':
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls"))
    ]
