from django.conf.urls import url
# from django.contrib import admin
from views import Welcome, Note, Delete, Update
from . import views


urlpatterns = [
	url(r'^$', Welcome.as_view(), name='welcome'),
	url(r'^notes$', Note.as_view(), name='notes'),
	url(r'^delete$', Delete.as_view(), name='delete'),
	url(r'^update$', Update.as_view(), name='update'),

]