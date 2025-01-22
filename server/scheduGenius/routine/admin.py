from django.contrib import admin
from .models import Faculty, Course, FacultyCourse, Classroom, Period, MasterRoutine

admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(FacultyCourse)
admin.site.register(Classroom)
admin.site.register(Period)
admin.site.register(MasterRoutine)
