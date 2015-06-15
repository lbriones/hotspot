from django.conf.urls import patterns, url

urlpatterns = patterns('cpanel.views',
	url(r'^$', 'index_view', name="index"),
	)