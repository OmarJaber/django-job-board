# Generated by Django 4.1.6 on 2023-03-30 08:50

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_job_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=job.models.image_upload),
        ),
    ]
