from django.db import models
from django.contrib.auth.models import User
# from string import join
from django.core.mail import send_mail
#from geoposition.fields import GeopositionField
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, unique = True, related_name="profile")
	#name = models.CharField(max_length=50, blank=False)
	phone_number = models.CharField(max_length=20, blank=True)
	can_cook = models.BooleanField()
	# profile_picture = models.ImageField(upload_to="profile-pictures", blank=True)
	rate = models.IntegerField()

class RequestManager(models.Manager):
	def create_request(self, uid, order, info, lon, lat):
		request = self.create(uid = uid, 
							  order = order, 
							  lon = lon, 
							  lat = lat, 
							  info = info)
		request.save()
		return request

class Request(models.Model):
	uid = models.ForeignKey(User)
	order = models.CharField(max_length=140, blank=False)
	info = models.CharField(max_length=200, blank=True) 
	lat = models.FloatField(blank=False)
	lon = models.FloatField(blank=False)
	objects = RequestManager()


	def __unicode__(self):
		return "Request " + str(self.id) + " " + self.order 

	@staticmethod
	def get_request(user):
		return Request.objects.filter(uid=user.id)

class StateManager(models.Manager):
	def create_state(self, state):
		state = self.create(state = state)
		state.save()
		return state

class State(models.Model):
	state = models.CharField(max_length=10, blank=False)
	objects = StateManager()

	def __unicode__(self):
		return "State " + state 

class TransactionManager(models.Manager):
	def create_transaction(self, rid, uid, stateid):
		transaction = self.create(rid=rid, uid=udi, stateid=stateid)
		transaction.save()
		return transaction

class Transaction(models.Model):
	rid = models.ForeignKey(Request)
	uid = models.ForeignKey(User)
	stateid = models.ForeignKey(State)
	offer = models.FloatField()
	read = models.BooleanField()
	approve = models.BooleanField()
	objects = TransactionManager()

	def __unicode__(self):
		return "Transaction " + str(self.id)

	@staticmethod
	def get_transaction(user):
		return Transaction.objects.filter(uid=user.id)	# Might need to change

class ReviewManager(models.Manager):
	def create_review(self, tid, u1id, u2id, stars, comment):
		review = self.create(tid=tid, u1id=u1id, u2id=u2id, stars=stars, comment=comment)
		review.save()
		return review

class Review(models.Model):
	tid = models.ForeignKey(Transaction)
	u1id = models.ForeignKey(User, related_name="u1id")
	u2id = models.ForeignKey(User, related_name="u2id")
	stars = models.IntegerField()
	comment = models.CharField(max_length=140, blank=False)
	objects = ReviewManager()
	
	def __unicode__(self):
		return "Review " + str(self.id)

class ActiveUserManager(models.Manager):
	def create_active_user(self, uid, lng, lat):
		active_user = self.create(uid=uid, lng=lng, lat=lat)	
		active_user.save()
		return active_user

class ActiveUser(models.Model):
	uid = models.ForeignKey(User)
	lng = models.FloatField(blank=False)
	lat = models.FloatField(blank=False)
	objects = ActiveUserManager()

	def __unicode__(self):
		return "Active User: " + str(uid)
