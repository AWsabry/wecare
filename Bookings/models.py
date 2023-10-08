from django.db import models
from Nurse.models import Nurse
from Register_Login.models import Profile

# Create your models here.

class Booking(models.Model):
    user = models.OneToOneField(to= Profile, on_delete=models.CASCADE,unique=True, related_name='user')
    nurse =  models.OneToOneField(to= Nurse, on_delete=models.CASCADE,unique=True, related_name='nurse')
    booking_time =  models.DateTimeField(max_length=20, unique=True, )
    hour =  models.CharField(max_length=30,blank=True,null=True)
    date = models.CharField(max_length=30,blank=True,null=True)
    city = models.CharField(max_length=30,blank=True,null=True)
    done = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.full_name
    class Meta:
        verbose_name_plural = "Bookings"
        verbose_name = "Booking"