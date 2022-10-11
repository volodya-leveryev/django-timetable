from django.contrib import admin

from timetable import models


@admin.register(models.StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Semester)
class SemesterAdmin(admin.ModelAdmin):
    pass
