from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
		url(r'^login$', 'core.views.login',  name='login'),
		url(r'^request$', 'core.order-request.request',  name='request'),
		url(r'^send$', 'core.order-request.send',  name='send'),
)