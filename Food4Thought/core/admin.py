from django.contrib import admin
from core.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'user_profile'

class UserProfileAdmin(UserAdmin):
    inlines=(UserProfileInline,)

class RequestAdmin(admin.ModelAdmin):
    list_display = ['uid', 'order', 'info', 'where']

class StateAdmin(admin.ModelAdmin):
    list_display = ['state']

class TransactionAdmin(admin.ModelAdmin):
    list_display  = ['rid', 'uid', 'stateid']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['tid', 'u1id', 'u2id', 'stars', 'comment']

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
admin.site.register(Request , RequestAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Review, ReviewAdmin)