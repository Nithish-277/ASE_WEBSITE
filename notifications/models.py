from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime

class Post(models.Model):
    problem_name = models.CharField('Problem Name',max_length=120)
    medicine_name  = models.CharField('Medicine Name',max_length=120)
    start_date = models.DateTimeField('start date',default= timezone.now)
    end_date = models.DateTimeField('end date')
    select_time = models.TimeField(auto_now=False, auto_now_add=False,default= datetime.now())
    email_id= models.EmailField(default='sivasaikrishna.n18@gmail.com')

    def __str__(self):
        return self.medicine_name