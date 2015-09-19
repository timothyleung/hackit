from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
		url(r'^login$', 'core.views.login',  name='login'),

)