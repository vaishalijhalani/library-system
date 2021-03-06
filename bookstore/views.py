# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import render
from django.template import loader
from models import Book
from form import checkoutForm

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect

def home(request):
	category = request.GET.get('category')
	if category:
		all_books = Book.objects.filter(category = category)
	else:
		all_books = Book.objects.all()

	all_category =[]
	for b in Book.objects.all():
		all_category.append(b.category)
	all_category = list(set(all_category))
	context = {'all_books':all_books, 'all_category':all_category}
	template = loader.get_template('home.html')
	
	return HttpResponse(template.render(context,request))


def product(request):
	isbn = request.GET.get('isbn')
	all_books = Book.objects.filter(isbn = isbn)
	all_category =[]
	for b in Book.objects.all():
		all_category.append(b.category)
	all_category = list(set(all_category))
	context = {'book':all_books[0],'all_category':all_category}
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
	if request.method=='POST':
		context = {}
		template = loader.get_template('thankyou.html')
		return HttpResponse(template.render(context,request))
	form = checkoutForm()
	context = {'form':form}
	template = loader.get_template('checkout.html')
	return HttpResponse(template.render(context,request))




