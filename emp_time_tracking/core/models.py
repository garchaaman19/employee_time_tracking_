from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    email=models.EmailField()    
    class Meta:
        db_table="user"


class TimeEntry(models.Model):
    clock_in=models.DateTimeField(null=True)
    clock_out=models.DateTimeField(null=True)
    user=models.ForeignKey("User",related_name="user_time_entry",on_delete=models.DO_NOTHING,default=None)

    class Meta:
        db_table="time_entry"
