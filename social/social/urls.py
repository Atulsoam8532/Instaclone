"""social URL Configuration

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
from django.urls import path
from social_media import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',views.logins,name='login'),
    path('signup/',views.singup,name='signup'),
    path('logout/',views.logouts,name='logout'),
    path('profile/',views.profiles,name='profile'),
    path('search/',views.search,name='search'),
    path('follow/<int:id>/<username>',views.follow,name='follow'),
    path('follow_profile/<int:id>/<username>',views.follow_profile,name='follow_profile'),
    path('follow_custom/<int:id>/<user>/<username>',views.follow_custom,name='follow_custom'),
    path('upload/',views.upload_post,name='upload'),
    path('edit/',views.edit,name='edit'),
    path('follower/<user>/',views.follow_list,name='follower'),
    path('following/<user>/',views.following,name='following'),
    path('like/<int:id>/',views.like,name='like'),
    path('reel',views.reel_show,name='reel'),
    path('upload_reel',views.upload_reel,name='upload_reel'),
    path('chat/<int:id>',views.chat,name='chat'),
    path('room/<int:id>',views.room,name='room'),
    path('showchats',views.showchat,name='showchats'),
    path('comment/<int:id>',views.add_comment,name='comment'),
    path('showprofile/<int:id>/<str:user>/',views.clicked_profile,name='showprofile'),
    path('grid/',views.grid,name='grid'),
    path('save/<int:id>',views.save_post,name='save'),
    path('saved_post/',views.show_save_post,name='savedpost')
    
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
