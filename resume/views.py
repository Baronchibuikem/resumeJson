import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.views import View

from resume.models import Profile


class ResumeView(View):
    def get(self) -> HttpResponse:
        """Retrieve all the data in the Profile db."""
        profile = Profile.objects.prefetch_related().last()

        if profile is not None:
            json_data = json.dumps(
                {
                    "profile": {
                        "fullname": profile.profile.name,
                        "label": profile.profile.label,
                        "phone number": str(profile.profile.phone),
                        "website": profile.profile.website,
                        "summary": profile.profile.summary,
                    },
                    "socials": [
                        {
                            "username": social.username,
                            "network": social.network,
                            "url": social.url,
                        }
                        for social in profile.social.all()
                    ],
                    "address": [
                        {
                            "city": profile.address.city,
                            "state": profile.address.state,
                            "country code": profile.address.country_code,
                            "country": profile.address.country,
                            "postal code": str(profile.address.postal_code),
                        }
                        if profile.address is not None
                        else {}
                    ],
                    "education": [
                        {
                            "institution": education.institution,
                            "course enrolled in": education.course_enrolled,
                            "study type": education.study_type,
                            "start date": str(education.start_date),
                            "end date": str(education.end_date),
                        }
                        for education in profile.education.all()
                    ],
                    "skills": [
                        {
                            "name": skill.name,
                            "level": skill.level,
                            "keywords": skill.keywords,
                        }
                        for skill in profile.skill.all()
                    ],
                    "work history": [
                        {
                            "company": work.company,
                            "position": work.position,
                            "company_website": work.website,
                            "start date": str(work.start_date),
                            "end date": str(work.end_date),
                            "company_summary": work.company_summary,
                            "achievements": work.highlight,
                        }
                        for work in profile.work_history.all()
                    ],
                }
            )
            return HttpResponse(
                json_data,
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        return HttpResponse(
            "No profile found",
            status=status.HTTP_200_OK,
            content_type="application/json",
        )
