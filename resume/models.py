from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid
from resumejson.storage_backends import PublicMediaStorage
from resume.utils import generic_documents_directory


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country_code = models.CharField(max_length=5, null=True, blank=True)
    country = models.CharField(max_length=25, null=True, blank=True)
    postal_code = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.country


class SocialProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    network = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.network


class WorkHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    company = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    website = models.URLField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    company_summary = models.CharField(max_length=255, null=True, blank=True)
    highlight = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.company


class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    institution = models.CharField(max_length=100, null=True, blank=True)
    course_enrolled = models.CharField(max_length=100, null=True, blank=True)
    study_type = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.institution


class Publication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(max_length=255, null=True, blank=True)
    published_on = models.CharField(max_length=100, null=True, blank=True)
    date_published = models.DateField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    level = models.CharField(max_length=100, null=True, blank=True)
    keywords = ArrayField(models.CharField(max_length=100), null=True, blank=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    language = models.CharField(max_length=100, null=True, blank=True)
    fluency = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.language


class Interest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    keyword = ArrayField(models.CharField(max_length=100), null=True, blank=True)

    def __str__(self):
        return self.name


class Reference(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    reference = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class PersonalDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=50, null=True, blank=True)
    label = models.CharField(max_length=50, null=True, blank=True)
    picture = models.ImageField(
        upload_to=generic_documents_directory,
        null=True,
        blank=True,
        storage=PublicMediaStorage(),
    )
    phone = PhoneNumberField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    profile = models.ForeignKey(
        "resume.PersonalDetail", null=True, blank=True, on_delete=models.CASCADE
    )
    social = models.ManyToManyField(
        "resume.SocialProfile", blank=True, related_name="social_profiles"
    )
    address = models.ForeignKey(
        "resume.Location", null=True, blank=True, on_delete=models.CASCADE
    )
    reference = models.ManyToManyField(
        "resume.Reference", blank=True, related_name="profile_reference"
    )
    interest = models.ManyToManyField(
        "resume.Interest", blank=True, related_name="interest"
    )
    language = models.ManyToManyField(
        "resume.Language", blank=True, related_name="profile_language"
    )
    skill = models.ManyToManyField(
        "resume.Skill", blank=True, related_name="profile_skill"
    )
    publication = models.ManyToManyField(
        "resume.Publication", blank=True, related_name="profile_publication"
    )
    education = models.ManyToManyField(
        "resume.Education", blank=True, related_name="profile_education"
    )
    work_history = models.ManyToManyField(
        "resume.WorkHistory", blank=True, related_name="profile_work_history"
    )

    def __str__(self):
        return self.profile.name
