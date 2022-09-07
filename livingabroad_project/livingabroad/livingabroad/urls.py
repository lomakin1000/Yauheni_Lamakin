"""livingabroad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  #При переходе по адресу admin - будет открываться приложение admin
    path('',include('main.urls')),#добавили путь к главной странице приложения main
    path('vacancies/',include('vacancies.urls')),
    path('forum/',include('forum.urls')),
    path('rent/',include('rent.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



# Отслеживаем различные url-адреса