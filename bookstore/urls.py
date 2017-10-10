from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^bookstore/product/',views.product, name='product'),
    #url(r"^signup/$", views.signup, name="account_signup"),
    #url(r"^login/$", views.login, name="account_login"),
    #url(r"^logout/$", views.logout, name="account_logout"),
    url(r'^profile/$',views.userprofile,name='proflie'),
    url(r'^bookstore/checkout/$',views.checkout,name='checkout'),
   
]