from django.shortcuts import render
from .forms import UploadFileForm


def home(request):
    foi_salvo = False
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form_upload = form.save(commit=False)
            # form_upload.uploadfile = request.FILES['uploadFile']
            form_upload.save()
            foi_salvo = True
        form = UploadFileForm()
    else:
        form = UploadFileForm()
    context = {"form": form, "foi_salvo": foi_salvo}
    return render(request, "challengebe/home.html", context)
