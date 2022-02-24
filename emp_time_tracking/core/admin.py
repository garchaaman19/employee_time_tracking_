import imp
from django.contrib import admin
from .models import User,TimeEntry
# Register your models here.
admin.site.register(User)
admin.site.register(TimeEntry)
