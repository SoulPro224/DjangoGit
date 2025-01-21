"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings

from debug_toolbar.toolbar import debug_toolbar_urls

from users.views import CustomLoginView
from users.views import CustomUserCreationView
from users.views import ActivationUserView
from users.views import ProfileUserView
from users.views import LogoutView


urlpatterns = [
    path('', ProfileUserView.as_view(), name='home'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/create/', CustomUserCreationView.as_view(), name='register'),
    path('accounts/activation/<uid>/<token>', ActivationUserView.as_view(), name='confirm_user_activation'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
] + debug_toolbar_urls()
