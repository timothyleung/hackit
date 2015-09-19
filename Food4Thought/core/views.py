from forms import *
from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.db import transaction
from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse


# Create your views here.

#def login(request):
#	return render(request, 'login.html', {})
@login_required
def home(request):
	profile, created = UserProfile.objects.get_or_create(user=request.user, defaults={'can_cook':False, 'rate':0,})
	return render(request, 'home.html', {})


def go_to_register_page(request):
	return render(request, 'register.html', {'registration_form': RegistrationForm})

def register(request):
	# do the registration here and go back to index page 
	# or just login directly 
	print "Register"
	if request.method == "GET":
		return render(reverse('home'))

	context = {}
	form = RegistrationForm(request.POST)
	context['registration_form']=form
	if not form.is_valid():
		print "REgistration Form is not valid!"
	new_user = User.objects.create_user(first_name=form.cleaned_data['name'],
                                        password=form.cleaned_data['password1'],
                                        username=form.cleaned_data['email'])   

	new_user.save()
	profile, created = UserProfile.objects.get_or_create(user=new_user, defaults={'phone_number':form.cleaned_data['phone_number'],
								 'can_cook':False, 'rate':0,})
	print created 
	profile.phone_number = form.cleaned_data['phone_number']
	profile.can_cook = False # By default it is false 
	profile.rate = 0 # by default, rate = 0 
	new_user.save()
	profile.save()
	new_user = authenticate(username=form.cleaned_data['email'],
                          password=form.cleaned_data['password1'])

	login(request, new_user)

    # login automatically after registration 
	return redirect(reverse('home'))


