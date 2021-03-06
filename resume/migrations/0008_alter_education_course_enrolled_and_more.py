# Generated by Django 4.0.2 on 2022-02-28 08:06

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_alter_education_id_alter_interest_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='course_enrolled',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3dcce514-478b-4d0a-94b0-713385858a6e'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='education',
            name='institution',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='study_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='interest',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e9c1bf02-9822-4480-a56f-c0ab9033198b'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='interest',
            name='keyword',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='interest',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='fluency',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b8d50bb2-58bd-4b25-9f2b-9500d3c99c2a'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='language',
            name='language',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.UUIDField(default=uuid.UUID('49d38b61-a1ec-4cc2-b705-6c83168941f8'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e0000b79-f49e-4b8c-adc9-2c89a43f729b'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('85427014-3889-4215-8642-a665af3ed342'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date_published',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='id',
            field=models.UUIDField(default=uuid.UUID('73402a56-fed0-46a2-b822-469a1a97b978'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='publication',
            name='published_on',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reference',
            name='id',
            field=models.UUIDField(default=uuid.UUID('70a6daf4-0fbb-4f7e-abfd-371e0ed9bbd9'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reference',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4dc255fc-c0f5-4265-937a-5f2e56954269'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='skill',
            name='keywords',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='socialprofile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('585722f7-c9a4-4ae6-8366-e33b17f1b170'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='socialprofile',
            name='network',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='socialprofile',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='socialprofile',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='workhistory',
            name='company_summary',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='workhistory',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workhistory',
            name='id',
            field=models.UUIDField(default=uuid.UUID('67f9bd05-a3f4-4ba3-8ed3-ff8bee5b0a7a'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='workhistory',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workhistory',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
