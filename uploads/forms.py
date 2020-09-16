from django import forms
from django.forms import ModelForm

from uploads.models import Upload_prescription,Upload_reports ,Queries

class PostForm(ModelForm):
    class Meta:
        model=Upload_prescription 
        fields=['hospital_name','disease_name','date','prescription_file']

class PostForm2(ModelForm):
    class Meta:
        model = Upload_reports
        fields=['diagnostics_name','report_type','date','report_file']      

class Form(ModelForm):
    class Meta:
        model = Queries
        fields = ['first', 'last', 'email', 'mobile','message']  


