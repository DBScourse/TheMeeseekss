# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
import db_handler as dbhandler
import django.core.exceptions
from django.views.decorators.csrf import csrf_exempt
import django.db
import django.db.models.sql
import hashlib
import json


@csrf_exempt
def generate_playlist(request):
    response = {}
    if request.method != 'POST':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        body = json.loads(request.body)
        response['data'] = dbhandler.create_playlist(body['username'], body['danceability'],
                                                     body['energy'],
                                                    body['playlist_name'], body['tags'])
        stat = 200
        response['status_message'] = 'Playlist generated successfully'
    except django.db.models.sql.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except Exception as err:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task: {}'.format(str(err))
    return JsonResponse(response, status=stat)

@csrf_exempt
def login(request):
    response = {}
    if request.method != 'POST':
        response['is_valid'] = False
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)

    try:
        # assuming input validation is done front-end
        body = json.loads(request.body)
        hcode = hashlib.md5(body['password']).hexdigest()
        if dbhandler.get_password(body['username']) == hcode:
            response['is_valid'] = True
            stat = 200
            response['status_message'] = 'Logged in successfully'
        else:
            response['is_valid'] = False
            stat = 401
            response['status_message'] = 'Bad Credentials'
    except django.db.models.sql.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Unknown Username'
    except Exception as err:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task: {}'.format(str(err))

    return JsonResponse(response, status=stat)

@csrf_exempt
def logout(request):
    response = {}
    if request.method != 'POST':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        # assuming input validation is done front-end
        body = json.loads(request.body)
        if not dbhandler.is_user(body['username']):
            stat = 403
            response['status_message'] = 'Invalid username'
            return JsonResponse(response, status=stat)
        stat = 200
        response['status_message'] = 'Logged out successfully'
    except django.db.models.sql.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except Exception as err:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task: {}'.format(str(err))
    return JsonResponse(response, status=stat)

@csrf_exempt
def register(request):
    response = {}
    if request.method != 'POST':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        # assuming input validation is done front-end
        body = json.loads(request.body)
        if dbhandler.is_user(body['username']):
            stat = 403
            response['status_message'] = 'Username is taken. Please try another'
            return JsonResponse(response, status=stat)
        hcode = hashlib.md5()
        hcode.update(body['password'])
        dbhandler.add_user(body['username'], hcode.hexdigest())
        # User is not logged in
        stat = 200
        response['status_message'] = 'Registered successfully'
    except django.db.models.sql.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except Exception as err:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task: {}'.format(str(err))
    return JsonResponse(response, status=stat)

@csrf_exempt
def free_search(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        response['data'] = dbhandler.search(request.GET['search_query'])
        stat = 200
        response['status_message'] = 'Data pulled successfully'
    except django.db.models.sql.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except Exception as err:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task: {}'.format(str(err))
    return JsonResponse(response, status=stat)

@csrf_exempt
def get_user_playlists(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        response['data'] = dbhandler.get_user_data(request.GET['username'])
        stat = 200
        response['status_message'] = 'Data pulled successfully'
    except django.db.models.sql.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except Exception as err:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task: {}'.format(str(err))
    return JsonResponse(response, status=stat)

@csrf_exempt
def add_song_to_playlist(request):
    response = {}
    if request.method != 'POST':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        body = json.loads(request.body)
        dbhandler.update_playlist(body['username'], body['song_id'])
        stat = 200
        response['status_message'] = 'Playlist updated successfully'
    except django.db.models.sql.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except Exception as err:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task: {}'.format(str(err))
    return JsonResponse(response, status=stat)

@csrf_exempt
def get_user_playlist_by_id(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        response['data'] = dbhandler.get_tracks_by_playlist_id(request.GET['username'], request.GET['playlist_id'])
        stat = 200
        response['status_message'] = 'Playlist updated successfully'
    except django.db.models.sql.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except Exception as err:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task: {}'.format(str(err))
    return JsonResponse(response, status=stat)

@csrf_exempt
def get_lyrics_by_track_id(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        response['data'] = dbhandler.get_lyrics_by_track_id(request.GET['lyrics_id'])
        stat = 200
        response['status_message'] = 'Playlist updated successfully'
    except django.db.models.sql.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except Exception as err:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task: {}'.format(str(err))
    return JsonResponse(response, status=stat)

@csrf_exempt
def get_artist_recommendation_from_last_playlist(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        response['data'] = dbhandler.get_artist_recommendation_from_last_playlist(request.GET['username'])
        stat = 200
        response['status_message'] = 'Playlist updated successfully'
    except django.db.models.sql.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except Exception as err:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task: {}'.format(str(err))
    return JsonResponse(response, status=stat)

@csrf_exempt
def get_top_artist_and_track(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        response['data'] = dbhandler.get_top_artist_top_track()
        stat = 200
        response['status_message'] = 'Playlist updated successfully'
    except django.db.models.sql.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except Exception as err:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task: {}'.format(str(err))
    return JsonResponse(response, status=stat)

@csrf_exempt
def get_tag_recommendations(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        response['data'] = dbhandler.get_tag_recommendations(request.GET['username'])
        stat = 200
        response['status_message'] = 'Playlist updated successfully'
    except django.db.models.sql.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except Exception as err:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task: {}'.format(str(err))
    return JsonResponse(response, status=stat)

@csrf_exempt
def artist_songs(request):
    response = {}
    if request.method != 'GET':
        stat = 400
        response['status_message'] = 'Illegal request. Please try again'
        return JsonResponse(response, status=stat)
    try:
        response['data'] = dbhandler.get_tracks_by_artist(request.GET['id'])
        stat = 200
        response['status_message'] = 'Playlist updated successfully'
    except django.db.models.sql.EmptyResultSet:
        stat = 404
        response['status_message'] = 'Empty result set'
    except Exception as err:
        stat = 503
        response['status_message'] = 'An error has occurred while performing the task: {}'.format(str(err))
    return JsonResponse(response, status=stat)
