# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
import db_handler as dbhandler
import user_log
import django.core.exceptions
import django.db


# Create your views here.
def generate_playlist(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    if not user_log.user_check(request.GET['username']):
        stat = 401
        response['status_message'] = 'User must be logged in'
        return JsonResponse(response, status=stat)
    try:
        response['data'] = dbhandler.update_user_history(request.GET['username'], request.GET['danceability'], request.GET['energy'],
                                      request.GET['tags'], request.GET['playlist_name'])
        # response['data'] = dbhandler.get_playlist(request.body['danceability'], request.body['energy'], request.body['tags'])
        stat = 200
        response['status_message'] = 'Playlist generated successfully'
    except django.core.exceptions.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except django.db.Error:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task'
    return JsonResponse(response, status=stat)


def login(request):
    response = {}
    if request.method != 'POST':
        response['is_valid'] = False
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)

    try:
        # assuming input validation is done front-end
        if dbhandler.get_password(request.body['username']) == request.body['password']:
            response['is_valid'] = True
            user_log.user_login(request.body['username'])
            stat = 200
            response['status_message'] = 'Logged in successfully'
        else:
            response['is_valid'] = False
            stat = 401
            response['status_message'] = 'Bad Credentials'
    except django.core.exceptions.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except django.db.Error:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task'

    return JsonResponse(response, status=stat)


def logout(request):
    response = {}
    if request.method != 'POST':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        # assuming input validation is done front-end
        if not dbhandler.is_user(request.body['username']):
            stat = 403
            response['status_message'] = 'Invalid username'
            return JsonResponse(response, status=stat)
        if not user_log.user_check(request.body['username']):
            stat = 403
            response['status_message'] = 'User not logged in'
            return JsonResponse(response, status=stat)
        user_log.user_logout(request.body['username'])
        stat = 200
        response['status_message'] = 'Logged out successfully'
    except django.core.exceptions.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except django.db.Error:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task'
    return JsonResponse(response, status=stat)


def register(request):
    response = {}
    if request.method != 'POST':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        # assuming input validation is done front-end
        if dbhandler.is_user(request.body['username']):
            stat = 403
            response['status_message'] = 'Username is taken. Please try another'
            return JsonResponse(response, status=stat)

        dbhandler.add_user(request.body['username'], request.body['password'])
        # User is not logged in
        stat = 200
        response['status_message'] = 'Registered successfully'
    except django.core.exceptions.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except django.db.Error:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task'
    return JsonResponse(response, status=stat)


def user_page(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        response['user_data'] = dbhandler.get_user_data(request.GET['username'])
        stat = 200
        response['status_message'] = 'Data pulled successfully'
        # Assuming the user is logged in - validated in front end
    except django.core.exceptions.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except django.db.Error:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task'
    return JsonResponse(response, status=stat)


def free_search(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        response['search_result'] = dbhandler.search(request.GET['search_query'])
        stat = 200
        response['status_message'] = 'Data pulled successfully'
    except django.core.exceptions.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except django.db.Error:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task'
    return JsonResponse(response, status=stat)


def get_user_playlists(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        response['user_data'] = dbhandler.get_user_data(request.GET['username'])
        stat = 200
        response['status_message'] = 'Data pulled successfully'
    except django.core.exceptions.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except django.db.Error:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task'
    return JsonResponse(response, status=stat)


def add_song_to_playlist(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        dbhandler.update_playlist(request.GET['username'], request.GET['song_id'])
        stat = 200
        response['status_message'] = 'Playlist updated successfully'
    except django.core.exceptions.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except django.db.Error:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task'
    return JsonResponse(response, status=stat)


def get_user_playlist_by_id(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        response['playlist'] = dbhandler.get_tracks_by_playlist_name(request.GET['username'], request.GET['playlist_id'])
        stat = 200
        response['status_message'] = 'Playlist updated successfully'
    except django.core.exceptions.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except django.db.Error:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task'
    return JsonResponse(response, status=stat)


def get_lyrics_by_track_id(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        response['lyrics'] = dbhandler.get_lyrics_by_track_id(request.GET['track_id'])
        stat = 200
        response['status_message'] = 'Playlist updated successfully'
    except django.core.exceptions.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except django.db.Error:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task'
    return JsonResponse(response, status=stat)

################################ TODO #####################################
def get_recommendation_from_last_playlist(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        response['recommendation'] = dbhandler.get_recommendation_by_playlist(request.GET['username'])
        stat = 200
        response['status_message'] = 'Playlist updated successfully'
    except django.core.exceptions.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except django.db.Error:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task'
    return JsonResponse(response, status=stat)


def get_top_artist_and_track(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        response['tops'] = dbhandler.get_top_artist_top_track()
        stat = 200
        response['status_message'] = 'Playlist updated successfully'
    except django.core.exceptions.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except django.db.Error:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task'
    return JsonResponse(response, status=stat)

################################ TODO #####################################
def get_user_recommendations(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        response['recommendation'] = dbhandler.get_user_recommendations(request.GET['username'])
        stat = 200
        response['status_message'] = 'Playlist updated successfully'
    except django.core.exceptions.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except django.db.Error:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task'
    return JsonResponse(response, status=stat)