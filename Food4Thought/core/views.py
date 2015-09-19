from django.shortcuts import render
from core.models import Request
import json

# Create your views here.
def login(request):
	# -33.9174103,151.2313068
	r = Request.objects.all()
	return render(request, 'base.html', {'locations': r})