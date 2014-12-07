# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from django.template import loader, RequestContext
from django.shortcuts import render, render_to_response


def index(request):	
	'''
	page for output index
	'''
	t = loader.get_template('page_index.html')
	c = RequestContext(request, {})	
	
	return HttpResponse(t.render(c)) 	

