"""djangogirls URL Configuration

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
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls), # ð admin íėīė§ ëĐėļ ėŽėīíļ
    path('', index), # ð index íėīė§ ęē―ëĄ
    path('myuser/', include('myuser.urls')), # ð ëëĐėļ/myuser/ëĄ ė§ėíė ë
    path('board/', include('board.urls')), # ð ëëĐėļ/board/ëĄ ė§ėíė ë
]
