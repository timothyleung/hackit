from django.shortcuts import render
from core.models import Request
import json

# Required login
def request(request):
	all_waiting_requests = Request.objects.all()
	return render(request, 'order-request.html', {'locations': all_waiting_requests})

# Required login
def send(request):
	# Get all available cooks
	# all_available_cooks = Request.objects.all()

	# Get current location

	# Get order information

	# Save order information

	return render(request, 'send-request.html', {})