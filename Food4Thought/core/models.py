from django.db import models
from django.contrib.auth.models import User
# from string import join
from django.core.mail import send_mail
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, unique = True)
	name = models.CharField(max_length=50, blank=False)
	phone_number = models.CharField(max_length=20, blank=True)
	can_cook = models.BooleanField()
	profile_picture = models.ImageField(upload_to="profile-pictures", blank=True)
	rate = models.IntegerField()

class RequestManager(models.Manager):
	def create_menu(self, uid, order, info):
		request = self.create(uid = uid, order = order, where = where, info = info)
		request.save()
		return request

class Request(models.Model):
	uid = models.ForeignKey(User)
	order = models.CharField(max_length=140, blank=False)
	info = models.CharField(max_length=200, blank=True)
	where = models.CharField(max_length=140, blank=False)

	def __unicode__(self):
		return self.id

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

	def __unicode__(self):
		return sefl.state

class TransactionManager(models.Manager):
	def create_transaction(self, rid, uid, stateid):
		transaction = self.create(rid=rid, uid=udi, stateid=stateid)
		transaction.save()
		return transaction

class Transaction(models.Model):
	rid = models.ForeignKey(Request)
	uid = models.ForeignKey(User)
	stateid = models.ForeignKey(State)

	def __unicode__(self):
		return self.id

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

	def __unicode__(self):
		return self.id