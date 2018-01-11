from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_playlists', views.get_playlists, name="get_playlists")
]