

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.views.static import serve as static_serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),
]

# Media fayllarni (yuklangan rasmlarni) DEBUG holatidan qat'iy nazar
# har doim ko'rsatish uchun (kichik loyihalar uchun xavfsiz yechim).
urlpatterns += [
    re_path(
        r'^media/(?P<path>.*)$',
        static_serve,
        {'document_root': settings.MEDIA_ROOT},
    ),
]