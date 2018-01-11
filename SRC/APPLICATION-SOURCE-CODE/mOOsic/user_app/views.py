# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
import db_handler as dbhandler


def get_playlists(request):
    bala = dbhandler.sample_sql_query()
    response = [{'name': 'try', 'id': 1}, {'name': 'if', 'id': 2}, {'name': 'works', 'id': 3}]
    return JsonResponse(response, safe=False)

# Create your views here.
