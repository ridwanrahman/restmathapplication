# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.views import APIView
import json
# Create your views here.
# def index(request):
# 	return HttpResponse("hi")


class Index(APIView):
	def get(self, request):
		return HttpResponse("Get response")


class Equation(APIView):
	def post(self, request):
		json_str = request.body.decode(encoding='UTF-8')
		json_obj = json.loads(json_str)
		equation = json_obj['equation']
		print equation
		return HttpResponse("POST re")