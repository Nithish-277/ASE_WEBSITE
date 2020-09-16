from django.contrib import admin

# Register your models here.
from userinfo.models import UserProfileInfo,User

admin.site.register(UserProfileInfo)