from django.conf.urls import patterns, include, url
from core.forms import *

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    #url(r'^request$', 'core.order-request.request', name='request'),
    # url(r'^send$', 'core.order-request.send', name='send'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'login.html',
                                                        'authentication_form':UserAuthForm,
                                                        'extra_context': {'registration_form': RegistrationForm, 'request_form':RequestForm},
                                                    }, name='login'),
    url(r'^register$', 'core.views.register', name='register'),
    url(r'^go_to_register_page$', 'core.views.go_to_register_page', name='go_to_register_page'),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^request$', 'core.views.request_order', name='request_order'),
)
