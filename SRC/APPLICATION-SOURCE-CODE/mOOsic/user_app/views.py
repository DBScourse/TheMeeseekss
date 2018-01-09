# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import db_handler as dbhandler

from django.http import HttpResponse
from django.template import loader


def index(request):
    bala = dbhandler.sample_sql_query()
    template = loader.get_template('user_app/index.html')
    context = {'bala': bala}
    return HttpResponse(template.render(context, request))
# Create your views here.
