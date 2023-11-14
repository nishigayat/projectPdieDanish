from django.contrib import admin
from .models import Student,UTTK_Member,Lecturer,Register_Case,Disciplinary_Case
# Register your models here.

admin.site.register(Student)
admin.site.register(UTTK_Member)
admin.site.register(Lecturer)
admin.site.register(Register_Case)
admin.site.register(Disciplinary_Case)