# Generated by Django 2.0.1 on 2018-11-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_remove_medical_library_prevention'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_detail',
            name='dr_value',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_detail',
            name='hospital_value',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
