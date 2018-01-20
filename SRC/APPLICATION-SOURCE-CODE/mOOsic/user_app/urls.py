from django.conf.urls import url

from . import views

# TODO check regex
urlpatterns = [
    url(r'^get_playlists', views.get_user_playlists),
    url(r'^get_playlist', views.get_user_playlist_by_id),
    url(r'^get_lyrics', views.get_lyrics_by_track_id),
    url(r'^get_playlist_recommendation', views.get_recommendation_from_last_playlist),
    url(r'^get_tops', views.get_top_artist_and_track),
    url(r'^get_user_recommendation', views.get_tag_recommendations),
    url(r'^add_song_to_playlist', views.add_song_to_playlist),
    url(r'^create_new_playlist', views.generate_playlist),
    url(r'^free_search', views.free_search),
    url(r'^logout', views.logout),
    url(r'^login', views.login),
    url(r'^register', views.register),

]
