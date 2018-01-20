from django.conf.urls import url

from . import views

# TODO check regex
urlpatterns = [
    url(r'^get_playlists', views.get_user_playlists),  # get a list of the user's playlists
    url(r'^get_playlist', views.get_user_playlist_by_id),  # get a list of tracks by playlist id
    url(r'^get_lyrics', views.get_lyrics_by_track_id),  # get a track's lyrics by it's id
    url(r'^get_playlist_recommendation', views.get_artist_recommendation_from_last_playlist),  # get artist recommendation from the user's last playlist. requires username
    url(r'^get_tops', views.get_top_artist_and_track),  # get the top artist and top track, not parameters needed
    url(r'^get_user_recommendation', views.get_tag_recommendations),  # get tag recommendations by username
    url(r'^add_song_to_playlist', views.add_song_to_playlist),  # add song to playlist by  and tack id
    url(r'^create_new_playlist', views.generate_playlist),  # create new playlist with parameters: username, danceability, energy, tags, playlist name
    url(r'^free_search', views.free_search),  # free artist text search
    url(r'^logout', views.logout),  # logout the user with it's username
    url(r'^login', views.login),  # login the user with it's username and password
    url(r'^register', views.register),  # register new user with username and password

]
