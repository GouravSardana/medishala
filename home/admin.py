from django.contrib import admin
from home.models import Patient_Detail, Hospital, Medical_Library, Blood_Sample, Request_button
from import_export.admin import ImportExportModelAdmin


admin.site.register(Patient_Detail)
admin.site.register(Hospital)
admin.site.register(Blood_Sample)
admin.site.register(Request_button)

@admin.register(Medical_Library)
class PersonAdmin(ImportExportModelAdmin):
    pass
