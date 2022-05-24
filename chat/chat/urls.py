from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('groups/', include('groups.urls', namespace="groups")),
    path('chats/', include('chats.urls', namespace="chats")),
    path('channels/', include('users_channels.urls', namespace="channels")),
    path('auth/', include('users.urls', namespace="users")),
    path('info/', include('info.urls', namespace="info")),
    path('', include('homepage.urls', namespace="homepage")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
