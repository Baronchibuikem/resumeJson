from __future__ import annotations

from datetime import date
from decimal import Decimal
from typing import Any, Dict

from phonenumber_field.formfields import PhoneNumberField
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import JSONField, ModelSerializer, Serializer

from resume.models import SocialProfile


class SocialProfileSerializer(ModelSerializer[SocialProfile]):
    class Meta:
        model = SocialProfile
        fields = ["network", "username", "url"]
