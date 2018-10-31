"""MegaIndexof URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from .views import showlist,episodelist,seasonlist,videoplayer,searchView,process,qualitylist,viewredirect
urlpatterns = [
    path('',searchView),
    path('show',showlist),
    path('process',process),
    #path('seasons/<slug:shows>',seasonlist),
    #path('episode',episodelist),
    #path('quality',qualitylist),
    #path('videoplay',videoplayer),
    path('series/<str:shows>',viewredirect),
    path('series/<str:shows>/<int:season>',viewredirect),
    path('series/<str:shows>/<int:season>/<int:episode>',viewredirect),
    path('series/<str:shows>/<int:season>/<int:episode>/<str:quality>',viewredirect),
]
