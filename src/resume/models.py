from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid

# Create your models here.


class Location(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False
    )  # NOQA (ignore all errors on this line)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country_code = models.CharField(max_length=5)
    country = models.CharField(max_length=25)
    postal_code = models.IntegerField()


class SocialProfile(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False
    )  # NOQA (ignore all errors on this line)
    network = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    url = models.URLField()


class Basic(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False
    )  # NOQA (ignore all errors on this line)
    name = models.CharField(max_length=50, null=True, blank=True)
    label = models.CharField(max_length=50, null=True, blank=True)
    picture = models.ImageField(upload_to="")
    phone = PhoneNumberField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    social = models.ManyToManyField(
        "resume.SocialProfile", blank=True, related_name="social_profiles"
    )
    address = models.ForeignKey("resume.Location", null=True, on_delete=models.CASCADE)


class WorkHistory(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False
    )  # NOQA (ignore all errors on this line)
    company = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    company_summary = models.CharField(max_length=255, blank=True)
    highlight = ArrayField(models.CharField(max_length=255), null=True, blank=True)


class Education(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False
    )  # NOQA (ignore all errors on this line)
    institution = models.CharField(max_length=100, blank=True)
    course_enrolled = models.CharField(max_length=100, blank=True)
    study_type = models.CharField(
        max_length=100, blank=True, help_text="Bachelor Degree"
    )
    start_date = models.DateField()
    end_date = models.DateField()


class Publication(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False
    )  # NOQA (ignore all errors on this line)
    title = models.CharField(max_length=255, blank=True)
    published_on = models.CharField(max_length=100, blank=True)
    date_published = models.DateField()
    website = models.URLField(null=True, blank=True)


class Skill(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False
    )  # NOQA (ignore all errors on this line)
    name = models.CharField(max_length=100, blank=True)
    level = models.CharField(max_length=100, blank=True)
    keywords = ArrayField(models.CharField(max_length=100), null=True)


class Language(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False
    )  # NOQA (ignore all errors on this line)
    language = models.CharField(max_length=100, blank=True)
    fluency = models.CharField(max_length=100, blank=True)


class Interest(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False
    )  # NOQA (ignore all errors on this line)
    name = models.CharField(max_length=100, blank=True)
    keyword = ArrayField(models.CharField(max_length=100), null=True)


class Reference(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False
    )  # NOQA (ignore all errors on this line)
    name = models.CharField(max_length=100, blank=True)
    reference = models.TextField(null=True, blank=True)
