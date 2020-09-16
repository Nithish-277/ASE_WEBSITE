from django.contrib import admin

# Register your models here.

from uploads.models import Upload_prescription,Upload_reports

admin.site.register(Upload_prescription)
admin.site.register(Upload_reports)