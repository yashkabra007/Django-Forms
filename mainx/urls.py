from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact_form, name='contact'),
    url(r'^signup/$', views.signup, name='signup'),
    ]