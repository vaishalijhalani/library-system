# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	price = models.CharField(max_length=20)
	image = models.URLField(max_length=200)
	description = models.CharField(max_length=500)
	isbn = models.CharField(max_length=20,null=True)
	#publisher = models.CharField(max_length=50)
	category = models.CharField(max_length=50,null=True)


#class User(models.Model):
#	name = models.CharField(max_length=250)
#	emailid = models.CharField(max_length=100)
#	password = models.CharField(max_length=100)

