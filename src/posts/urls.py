from django.conf.urls import include, url
from django.contrib import admin


from .views import (
	post_list,
	post_list_newest,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
    url(r'^create/$', post_create),
	url(r'^newest/$', post_list_newest),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^$', post_list),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete)
    ]
