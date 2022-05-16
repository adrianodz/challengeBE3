from django.db import models
from django.utils import timezone


def path_to_upload(self, filename):
    extension = filename.split(".")[1]
    name = (
        str(timezone.now())
        .replace("-", "")
        .replace(":", "")
        .replace(" ", "-")
        .split(".")[0]
    )
    return f"{name}.{extension}"


class UploadFile(models.Model):
    created_date = models.DateField(verbose_name="Created Date", auto_now=True)
    uploadfile = models.FileField(
        verbose_name="Upload File", upload_to=path_to_upload, max_length=500
    )
