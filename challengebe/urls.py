from django.urls import path
from challengebe import views

app_name = "challengebe"

urlpatterns = [
    path("", views.home, name="home"),
]
