import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.views import View

from resume.utils import query_debugger
from resume.models import Basic, Education, Skill

# class SocialProfileView(APIView):
#     serializer_class = SocialProfileSerializer

#     def get(self, request: Request):
#         socials = SocialProfile.objects.all().first()

#         return Response(
#             SocialProfileSerializer(socials).data, status=status.HTTP_200_OK
#         )


class ResumeView(View):
    @query_debugger
    def get(self, request: Request):
        # make queries
        profile = Basic.objects.prefetch_related().last()
        education = Education.objects.all().last()
        skills = Skill.objects.all()

        json_data = json.dumps(
            {
                "basics": {
                    "fullname": profile.name,
                    "label": profile.label,
                    "phone number": str(profile.phone),
                    "website": profile.website,
                    "summary": profile.summary,
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
                    ],
                },
                "education": {
                    "institution": education.institution,
                    "course enrolled in": education.course_enrolled,
                    "study type": education.study_type,
                    "start date": str(education.start_date),
                    "end date": str(education.end_date),
                },
            }
        )
        return HttpResponse(
            json_data,
            status=status.HTTP_200_OK,
            content_type="application/json",
        )
