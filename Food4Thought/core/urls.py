from django.conf.urls import patterns, include, url
from forms import *

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^request$', 'core.order-request.request', name='request'),
    url(r'^send$', 'core.order-request.send', name='send'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'home.html',
                                                        'authentication_form':UserAuthForm,
                                                        'extra_context': {'registration_form': RegistrationForm},
                                                    }, name='login'),
    url(r'^register$', 'core.views.register', name='register'),
    url(r'^go_to_register_page$', 'core.views.go_to_register_page', name='go_to_register_page'),
)