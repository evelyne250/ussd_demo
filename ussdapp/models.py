from django.db import models
import uuid
from datetime import datetime
# Create your models here.
class Ussd(models.Model):
    msisdn = models.CharField(max_length=13)
    session_id = models.IntegerField(unique=True)
    input = models.CharField(max_length=40)
    newreq = models.BooleanField(default=False)
    # def __str__(self):
    #     return self.msisdn +  " My session is" + str(self.session_id) + "the new request is" + str(self.newreq) + "with short code =" + str(self.input)



