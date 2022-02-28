from django.contrib import admin

from resume.models import (
    Reference,
    Interest,
    Language,
    SocialProfile,
    PersonalDetail,
    Location,
    Education,
    Skill,
    Profile,
    WorkHistory,
)


admin.site.register(SocialProfile)
admin.site.register(PersonalDetail)
admin.site.register(Location)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Reference)
admin.site.register(Interest)
admin.site.register(Language)
admin.site.register(Profile)
admin.site.register(WorkHistory)
