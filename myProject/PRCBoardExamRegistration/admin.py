from django.contrib import admin
from .models import PersonalInfo,ExamHistory,EducationInfo,Application

admin.site.register(PersonalInfo)
admin.site.register(ExamHistory)
admin.site.register(EducationInfo)
admin.site.register(Application)
admin.site.site_header = "Professional Regulation Commission"
admin.site.site_title = "PRC Admin Portal"
admin.site.index_title = "PRC"
