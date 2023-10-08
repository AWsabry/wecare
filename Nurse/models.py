from django.db import models
from Register_Login.models import Profile


# Create your models here.


class Nurse(models.Model):
    user = models.OneToOneField(to= Profile, on_delete=models.CASCADE,unique=True, related_name='client')
    city = models.CharField(max_length=50,)
    phone_number =  models.CharField(max_length=20, unique=True, )
    age =  models.IntegerField(blank=True,null=True)
    gender = models.CharField(max_length=30,blank=True,null=True)
    is_active = models.BooleanField(default=False)
    years_of_experience = models.CharField(max_length=30,blank=True,null=True)
    national_id = models.CharField(max_length=30,blank=True,null=True)
    proof_of_experience = models.CharField(max_length=30,blank=True,null=True)
    available_times = models.CharField(max_length=30,blank=True,null=True)
    cv = models.CharField(max_length=30,blank=True,null=True)
    published = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.full_name
    class Meta:
        verbose_name_plural = "Nurses"
        verbose_name = "Nurse"


