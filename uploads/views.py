from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from .forms import *
from .models import  *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
import datetime,schedule
@login_required
def home(request):
    if request.method == 'POST':
        firstname = request.POST['first']
        lastname = request.POST['last']
        e = request.POST['email']
        mobile = request.POST['mobile']
        m = request.POST['message']
        form = Form(request.POST)
        if form.is_valid():
            save_it = form.save(commit = False)
            save_it.save()

            subject1 = 'Your Query has been Received'
            message1 = '''Your Query has been sent to our Team.
            We will be in touch soon'''
            from_email1 = settings.EMAIL_HOST_USER
            to_list1 = [save_it.email]

            subject2 = 'New Query has been Received'
            message2 = 'Name : ' + firstname + ' ' + \
                lastname + '\n' + 'Mobile : ' + mobile + '\n' + \
                'Email : ' + e + '\n' + 'Message : \n' + m

            from_email2 = settings.EMAIL_HOST_USER
            to_list2 = ['nikhil.a18@iiits.in','nithish.k18@iiits.in']

            m1 = (subject1, message1, from_email1,to_list1)
            m2 = (subject2, message2, from_email2, to_list2)
            send_mass_mail((m1, m2), fail_silently=False)
            messages.success(request, "Your Query has been successfully submitted..!!")
            return redirect('home')
    return render(request, 'uploads/homepage.html',{'title':'Home'})
@login_required
def forum(request):
    return render(request,'uploads/forums.html',{'title':'Forum'})
@login_required
def remainder(request):
    return render(request,'uploads/project.html',{'title':'Remainder'})
@login_required
def uploads(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        details = PostForm(request.POST,request.FILES)
        details2 = PostForm2(request.POST,request.FILES)
        details.instance.author = request.user
        details2.instance.author = request.user
        if details.is_valid():
            print("hi")
            post=details.save(commit=False)
            post.save()
            messages.success(request,"Data for Prescription Submitted Succesfully..!!")
            return redirect('Upload')
        elif details2.is_valid():
            post2 = details2.save(commit=False)
            post2.save()
            messages.success(request,"Data for Report Submitted Succesfully..!!")
            return redirect('Upload')
        else:
            return HttpResponse("None of the forms are filled!")
    else:
        return render(request,'uploads/upload.html',{'title':'Uploads'})

@login_required
def edit_prescription(request, pk):
    post = Upload_prescription.objects.get(id=pk)
    date = str(post.date)
    if request.method == 'POST':
        details = PostForm(request.POST, request.FILES)
        details.instance.author = request.user
        if details.is_valid():
            if len(request.FILES) == 0:
                details.instance.prescription_file = post.prescription_file
            post1 = details.save(commit=False)
            post1.save()
            if len(request.FILES) == 0:
                post.delete_not_file()
            else:
                print('ok3')
                post.delete()
            messages.success(request, "Data for Prescription Submitted Edited..!!")
        return redirect('searchprescription')

    return render(request, 'uploads/edit_prescription.html', {'post': post ,'date': date})

@login_required
def edit_report(request, pk):
    post = Upload_reports.objects.get(id=pk)
    date = str(post.date)
    print(post.report_file.url)
    if request.method == 'POST':
        details = PostForm2(request.POST, request.FILES)
        details.instance.author = request.user
        if details.is_valid():
            if len(request.FILES) == 0:
                details.instance.report_file = post.report_file
            post1 = details.save(commit=False)
            post1.save()
            if len(request.FILES) == 0:
                post.delete_not_file()
            else:
                print('ok3')
                post.delete()
            messages.success(
                request, "Data for Report Submitted Edited..!!")
        return redirect('searchreport')

    return render(request, 'uploads/edit_report.html', {'post': post, 'date': date})

@login_required
def temporary_files(request):
    prescriptions= Upload_prescription.objects.all()
    reports =Upload_reports.objects.all()
    return render(request,'uploads/files.html',{'prescriptions':prescriptions,'reports':reports})
@login_required
def delete_prescription(request, pk):
    if request.method == 'POST':
        file = Upload_prescription.objects.get(id=pk)
        file.delete()
    return redirect('searchprescription')
@login_required
def delete_report(request, pk):
    if request.method == 'POST':
        file = Upload_reports.objects.get(id=pk)
        file.delete()
    return redirect('searchreport')


dictonary_to_send_email = dict()
def sendmail1():
    d = datetime.date.today()
    d = str(d)
    if dictonary_to_send_email.get(d):
        email_list = dictonary_to_send_email[d]
        subject = 'Reminder To go to Hospital'
        message = '''You have set a Reminder to go to hospital Today'''
        from_email = settings.EMAIL_HOST_USER
        to_list = dictonary_to_send_email[d]
        send_mail(
            Subject,
            message,
            from_email,
            to_list,
            fail_silently=True,
        )


@login_required
def searchprescription(request):
    if request.method == 'POST':
        y = request.POST['date'][:4]
        m = request.POST['date'][5:7]
        d = request.POST['date'][8:]
        date_to_send_mail = y + '-' + d + '-' + m
        email = request.POST['email']
        if dictonary_to_send_email.get(date_to_send_mail):
            dictonary_to_send_email[date_to_send_mail].append(email)
        else:
            dictonary_to_send_email[date_to_send_mail] = []
            dictonary_to_send_email[date_to_send_mail].append(email)
        schedule.every().day.at("06:00").do(sendmail1)
        messages.info(
            request, "Reminder has been set to " + date_to_send_mail + ". You will get an reminder on " + date_to_send_mail + " to this mail "+email)
        return(redirect('searchprescription'))
    prescription= Upload_prescription.objects.filter(author = request.user)
    hospital_name_query = request.GET.get('hospital_name')
    disease_name_query = request.GET.get('disease_name')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')

    if hospital_name_query != '' and hospital_name_query is not None:
        prescription = prescription.filter(hospital_name__icontains = hospital_name_query)

    if disease_name_query != '' and disease_name_query is not None:
        prescription = prescription.filter(disease_name__icontains = disease_name_query)

    if date_min != '' and date_min is not None:
        prescription = prescription.filter(date__gte=date_min)

    if date_max != '' and date_max is not None:
        prescription = prescription.filter(date__lt=date_max)
    context = {
        'prescriptions':prescription,
        }
    return render(request,'uploads/prescriptionsearch.html',context)


dict_to_send_email = dict()
def sendmail2():
    d = datetime.date.today()
    d = str(d)
    if dictonary_to_send_email.get(d):
        email_list = dictonary_to_send_email[d]
        subject = 'Reminder To go to Hospital'
        message = '''You have set a Reminder to go to hospital Today'''
        from_email = settings.EMAIL_HOST_USER
        to_list = dictonary_to_send_email[d]
        send_mail(
            Subject,
            message,
            from_email,
            to_list,
            fail_silently=True,
        )

@login_required
def searchreport(request):
    if request.method == 'POST':
        y = request.POST['date'][:4]
        m = request.POST['date'][5:7]
        d = request.POST['date'][8:]
        date_to_send_mail = y + '-' + d + '-' + m
        email = request.POST['email']
        if dict_to_send_email.get(date_to_send_mail):
            dict_to_send_email[date_to_send_mail].append(email)
        else:
            dict_to_send_email[date_to_send_mail] = []
            dict_to_send_email[date_to_send_mail].append(email)
        schedule.every().day.at("06:00").do(sendmail2)
        messages.info(
            request, "Reminder has been set to " + date_to_send_mail + ". You will get an reminder on " + date_to_send_mail + " to this mail "+email)
        return(redirect('searchreport'))
    report= Upload_reports.objects.filter(author = request.user)
    diagnostics_name_query = request.GET.get('diagnostics_name')
    report_type_query = request.GET.get('report_type')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    if diagnostics_name_query != '' and diagnostics_name_query is not None:
        report = report.filter(diagnostics_name__icontains = diagnostics_name_query)
    if report_type_query != '' and report_type_query is not None:
        report = report.filter(report_type__icontains = report_type_query)
    if date_min != '' and date_min is not None:
        report = report.filter(date__gte=date_min)
    if date_max != '' and date_max is not None:
        report = report.filter(date__lt=date_max)
    context = {
        'reports':report,
        }
    return render(request,'uploads/reportsearch.html',context)
