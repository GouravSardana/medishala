# Generated by Django 2.0.1 on 2019-11-12 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_delete_medical_library'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient_detail',
            name='user',
        ),
        migrations.DeleteModel(
            name='Patient_Detail',
        ),
    ]