from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('films.urls')),

    path('director/new/', include('films.urls')),
    path('director/all', include('films.urls')),
    path('director/<int:pk>', include('films.urls')),
    path('director/<int:pk>/edit', include('films.urls')),
    path('director/search', include('films.urls')),

    path('genre/new', include('films.urls')),
    path('genre/all', include('films.urls')),
    path('genre/<int:pk>', include('films.urls')),
    path('genre/<int:pk>/edit/', include('films.urls')),
    path('genre/search', include('films.urls')),

    path('movie/new', include('films.urls')),
    path('movie/all', include('films.urls')),
    path('movie/<int:pk>/', include('films.urls')),
    path('movie/<int:pk>/edit/', include('films.urls')),
    path('movie/search', include('films.urls')),

    path('admin/', admin.site.urls),
    path('films/', include('films.urls')),

    re_path(r'users/(?P<user_id>\d+)/(?P<user_name>\D+/)', include('films.urls')),

    path('__debug__/', include('debug_toolbar.urls')),

    path('social_auth/', include('social_django.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
