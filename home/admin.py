from django.contrib import admin
from home.models import Blood_Sample, Request_button
from import_export.admin import ImportExportModelAdmin


# admin.site.register(Blood_Sample)
admin.site.register(Request_button)


@admin.register(Blood_Sample)
class PersonAdmin(ImportExportModelAdmin):
    pass
