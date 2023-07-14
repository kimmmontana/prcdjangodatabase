from django.contrib import admin
from .models import PersonalInfo,ExamHistory,EducationInfo,Application

admin.site.register(PersonalInfo)
admin.site.register(ExamHistory)
admin.site.register(EducationInfo)
admin.site.register(Application)
admin.site.site_header = "Professional Regulation Commission"

from django.contrib import admin

class CustomAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        ordering = {
            'PRCBOARDEXAMREGISTRATION': 0,
            'PersonalInfo': 1,
            'ExamHistory': 2,
            'EducationInfo': 3,
            'Application': 4,
        }
        app_dict = super().get_app_list(request)
        app_dict.sort(key=lambda x: ordering.get(x['name'], 999))
        return app_dict

admin_site = CustomAdminSite(name='customadmin')
