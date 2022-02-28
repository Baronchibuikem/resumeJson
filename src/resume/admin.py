from django.contrib import admin

from resume.models import SocialProfile, Basic, Location, Education


admin.site.register(SocialProfile)
admin.site.register(Basic)
admin.site.register(Location)
admin.site.register(Education)
