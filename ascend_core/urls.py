from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", include("apps.login.urls")),
    path("register/", include("apps.register.urls")),
    path("home/", include("apps.home.urls")),
    path("profile/", include("apps.user_profile.urls")),
    path("settings/", include("apps.user_settings.urls")),
    path("simulation/", include("apps.simulation.urls")),
    # Redirect root to home
    path("", lambda request: redirect("home:home")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
