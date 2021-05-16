from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import CSV, XLSX

from core.models import Student


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):

    list_display = ('id', 'first_name', 'last_name', 'registration_number', 'gender', 'date_of_admission')
    formats = [XLSX, CSV]
