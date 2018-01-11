# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
import db_handler as dbhandler


from django.http import HttpResponse
from django.template import loader


def index(request):
    bala = dbhandler.sample_sql_query()
    template = loader.get_template('user_app/index.html')
    context = {'bala': bala}
    return HttpResponse(template.render(context, request))




def get_playlists(request):
    bala = dbhandler.sample_sql_query()
    response = [{'name': 'try', 'id': 1}, {'name': 'if', 'id': 2}, {'name': 'works', 'id': 3}]
    return JsonResponse(response, safe=False)

# Create your views here.
