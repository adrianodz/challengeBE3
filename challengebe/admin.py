from django.contrib import admin
from .models import UploadFile


class UploadFileAdmin(admin.ModelAdmin):
    list_display = ["uploadfile", "created_date"]
    model = UploadFile


admin.site.register(UploadFile, UploadFileAdmin)
