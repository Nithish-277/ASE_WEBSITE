from django import forms
from django.forms import ModelForm

from notifications.models import Post

class PostForm(ModelForm):
    class Meta:
        model=Post 
        fields=['problem_name','medicine_name','start_date','end_date','select_time','email_id']