from django.urls import path

from resume.views import ResumeView

urlpatterns = [path("", ResumeView.as_view(), name="socialprofile")]
