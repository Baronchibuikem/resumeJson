# Generated by Django 4.0.2 on 2022-02-28 07:39

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_rename_postalcode_location_postal_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('5be81e1b-e9fc-41d3-a33e-1429e32c6c12'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('label', models.CharField(blank=True, max_length=50, null=True)),
                ('picture', models.ImageField(upload_to='')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('website', models.URLField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('131fa5c3-7929-4525-86a5-1d415119cdf3'), editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='education',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bfa0ddc8-fb36-44a1-a97d-38d6f05b9bb7'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='interest',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ab042f3c-8fb8-4408-921e-3532e0e3cd4b'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='language',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b7ecebf9-2c1c-49de-aa1c-9d425ef69365'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5deb8d9f-89a6-4d72-8996-d86cf95f64fe'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='publication',
            name='id',
            field=models.UUIDField(default=uuid.UUID('700336a9-c491-4f84-b628-77efaf77ef86'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reference',
            name='id',
            field=models.UUIDField(default=uuid.UUID('16c7e2a8-ecbd-4f18-9186-54efb61126da'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='skill',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9f423115-8586-4e5b-97b7-27809b95267f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='socialprofile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('68fae8b5-9aa0-4fb6-926c-6db1584651ee'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='workhistory',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bb213cb2-48f7-480f-b42a-4769720ac1d2'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Basic',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.location'),
        ),
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.ManyToManyField(blank=True, related_name='profile_education', to='resume.Education'),
        ),
        migrations.AddField(
            model_name='profile',
            name='interest',
            field=models.ManyToManyField(blank=True, related_name='interest', to='resume.Interest'),
        ),
        migrations.AddField(
            model_name='profile',
            name='language',
            field=models.ManyToManyField(blank=True, related_name='profile_language', to='resume.Language'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.personaldetails'),
        ),
        migrations.AddField(
            model_name='profile',
            name='publication',
            field=models.ManyToManyField(blank=True, related_name='profile_publication', to='resume.Publication'),
        ),
        migrations.AddField(
            model_name='profile',
            name='reference',
            field=models.ManyToManyField(blank=True, related_name='profile_reference', to='resume.Reference'),
        ),
        migrations.AddField(
            model_name='profile',
            name='skill',
            field=models.ManyToManyField(blank=True, related_name='profile_skill', to='resume.Skill'),
        ),
        migrations.AddField(
            model_name='profile',
            name='social',
            field=models.ManyToManyField(blank=True, related_name='social_profiles', to='resume.SocialProfile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='work_history',
            field=models.ManyToManyField(blank=True, related_name='profile_work_history', to='resume.WorkHistory'),
        ),
    ]