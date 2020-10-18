"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # django administration
    path("dj-admin/", admin.site.urls),
    # 3rd party
    path("accounts/", include("allauth.urls")),
    # local apps
    path("", include("pages.urls", namespace="pages")),
    path("blog/", include("blog.urls", namespace="blog")),
    path("profile/", include("users.urls", namespace="profile")),
]
