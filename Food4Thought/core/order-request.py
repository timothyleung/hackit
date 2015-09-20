from django.shortcuts import render
from core.models import Request
from core.models import User
import json

# Required login
def request(request):
	locations = Request.objects.all() 
	return render(request, 'order-request.html', {'locations': locations})

# Required login
def send(request):
	# Get all available cooks
	# all_available_cooks = Request.objects.all()

	# Get current location

	# Get order information

	# Save order information

	return render(request, 'send-request.html', {})