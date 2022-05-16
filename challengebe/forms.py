from django import forms
from .models import UploadFile


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ("uploadfile",)
        # widgets = {'uploadfile': forms.FileInput(attrs={'class': 'form-control', 'accept': 'application/xlsx'})}
