from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("member/", include("members.urls", namespace="members")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    # 앞에 admin 있는것을 숨겨줌
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
