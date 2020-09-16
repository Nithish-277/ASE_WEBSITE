from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.

#model for prescriptions
class Upload_prescription(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,default = None)
    hospital_name = models.CharField( max_length=50,blank=False,null=False)
    disease_name = models.CharField(max_length=15,blank=False,null=False)
    date = models.DateField(default=timezone.now)
    prescription_file = models.FileField(upload_to='files/prescriptions',default="Some File")

    def __str__(self):
        return self.hospital_name

    def delete(self, *args, **kwargs):
        self.prescription_file.delete()
        super().delete(*args, **kwargs)
    
    def delete_not_file(self, *args, **kwargs):
        super().delete(*args, **kwargs)
#model for reports
class Upload_reports(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,default = None)
    diagnostics_name = models.CharField(max_length=50,blank=False,null=False)
    report_type = models.CharField(max_length=20,blank=False,null=False)
    date = models.DateField(default=timezone.now)
    report_file = models.FileField(upload_to='files/reports',default="Some File")

    def __str__(self):
        return self.report_type


    def delete(self, *args, **kwargs):
        self.report_file.delete()
        super().delete(*args, **kwargs)

    def delete_not_file(self, *args, **kwargs):
        super().delete(*args, **kwargs)

class Queries(models.Model):
    first = models.CharField(max_length=50, blank=False, null=False)
    last = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=50)
    mobile = models.IntegerField()
    message = models.CharField(max_length=5000)