"""
URL configuration for evara project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from home.views import *
from accounts.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HOME,name='home'),
    path('login_registration/',AUTHENTICATE, name='login_registration'),
    path('registration/',Registration_user,name='registration'),
    path('otp_verify/',otp_verification, name='otp_verify'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    path('forgot-password/',reset_password,name='forgot_password'),
    path('otp-verification/<int:id>/', forgot_otp_verification, name='otp_verification'),
    path('reset-password-confirm/<int:id>/', reset_password_confirm, name='reset_password_confirm'),
    path('deshbord-account/',PAGE_ACCOUNT, name='dashboard'),
    path('account-details/',Account_details, name='account_details'),
    path('accounts/', include('allauth.urls')),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)