from os import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from members import views as members_views


urlpatterns = [
    path("", members_views.all_memebr_views, name="home"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    # 앞에 admin 있는것을 숨겨줌
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
