from django.urls import path

from resume.views import ResumeView, IndexView

urlpatterns = [
    path("", ResumeView.as_view(), name="socialprofile"),
    path("index", IndexView.as_view(), name="index"),
]
