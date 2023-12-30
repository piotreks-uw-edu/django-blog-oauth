from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("polling/", include("polling.urls")),
    path("", include("blogging.urls")),
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]
