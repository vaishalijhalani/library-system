# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import render
from django.template import loader
from models import Book

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect

def home(request):
	print request
	all_books = Book.objects.all()
	all_category = []
	for b in all_books:
		print all_category.append(b.category)
	all_category = list(set(all_category))
	# all_books = serializers.serialize("json", all_books)
	context = {'all_books':all_books, 'all_category':all_category}
	template = loader.get_template('home.html')
	return HttpResponse(template.render(context,request))


def product(request):
	context = {}
	template = loader.get_template('product.html')
	return HttpResponse(template.render(context,request))

@login_required
def userprofile(request):
	user = request.user
	context = {'user':user}
	template = "profile.html"
	return render(request,template,context)


@login_required
def checkout(request):
	context = {}
	template = "checkout.html"
	return render(request,template,context)




