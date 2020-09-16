from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=1)
    dob = models.DateField()
    Bloodgroup = models.CharField(max_length=2)
    phoneno = models.IntegerField()
    profile_pic = models.ImageField(default = "profile_pics/default.jpg",upload_to='profile_pics',blank=True)


    def __str__(self):
        return self.user.username

    def save(self):
        super().save()
        img = Image.open(self.profile_pic.path)
        print(self.profile_pic.path)
        if img.height > 300 or img.width > 300:
            output_size = (100, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

# def create_profile(sender,**kwargs):
#     if kwargs['created']:
#         user_profile = UserProfileInfo.objects.create(user = kwargs['instance'])
# post_save.connect(create_profile,sender = User)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

