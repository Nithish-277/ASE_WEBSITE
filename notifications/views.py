from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from notifications.forms import PostForm
from notifications.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from datetime import datetime
import schedule

def notification(request):

    if request.method == 'POST':
        print(request.POST)
        details = PostForm(request.POST,request.FILES)
        details.instance.author = request.user
        if details.is_valid():
            post=details.save(commit=False)
            post.save()
            messages.success(request,"Your REMINDER is Stored Succesfully..!!")
            return redirect('blog-notifications')
        else:
            return HttpResponse("None of the forms are filled!")
    else:
        return render(request, 'notifications/notification.html')

 # def temporary_files(request):
 #    notifications= notifications.objects.all()
 #    return render(request,'notification.html',{'notifications':notifications})



from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sender = 'nekkalapu25301@gmail.com'
receivers = ['nikhilesh.cherukuri001@gmail.com']

message = """From: From Person <nekkalapu25301@gmail.com>To: To Person <nikhilesh.cherukuri001@gmail.com>Subject: SMTP e-mail test This is a test e-mail message."""
MY_ADDRESS = 'nekkalapu25301@gmail.com'
PASSWORD = 'amma nanna'

notifications = Post.objects.all()
# smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
# smtpObj.starttls()
# smtpObj.login(MY_ADDRESS, PASSWORD)

# def sendmail(msg):
#     smtpObj.send_message(msg) 

# def demo():
#     print("Function Called")   

for notif in notifications:
        msg = MIMEMultipart()
        message = "Hi its time to take "+notif.medicine_name +" for "+notif.problem_name
        msg['From'] = MY_ADDRESS
        msg['To'] = notif.email_id  
        msg['Subject'] = notif.medicine_name + " Remainder."
        # smtpObj.sendmail(sender, receivers, message)
        msg.attach(MIMEText(message, 'plain'))
        # smtpObj.send_message(msg)
        # print(str(notif.select_time)[:-3])
        # # print(smtpObj.send_message(msg))
        # schedule.every().day.at(str(notif.select_time)[:-3]).do(demo)
        # print("Successfully sent email")
    
