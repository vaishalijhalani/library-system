from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name='home'),
    url(r'^product/',views.product, name='product'),
    url(r'^profile/',views.userprofile,name='proflie'),
    url(r'^checkout/',views.checkout,name='checkout')
]