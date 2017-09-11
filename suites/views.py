#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections
from django.utils.http import http_date
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import render_to_response, redirect

import json

from suites.models import NomeQuarto, ControleQuarto, Hospede
# Create your views here.

@require_http_methods(["GET"])
@csrf_exempt
def home(request):
	context = []
	datas = ControleQuarto.objects.all()
	for data in datas:
		context.append(data.to_dict())

	return render_to_response('home.json', json.dumps(context), content_type='application/json')
