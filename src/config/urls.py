from django.conf import settings
from django.contrib import admin
from django.urls import include, path

v1 = [
    # path("posts/", post.view),
]

api = [
    path("v1/", include(v1)),
    path("v2/", include(v1)),
]

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("auth/", include("apps.authentication.urls")),
    path("api/", include(api)),
]

if settings.DEBUG:
    # import debug_toolbar
    from django.conf.urls.static import static

    # from config.yasg import urlpatterns as yasg_docs

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    # urlpatterns += yasg_docs
