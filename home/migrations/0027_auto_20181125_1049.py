# Generated by Django 2.0.1 on 2018-11-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20181125_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient_detail',
            name='dr_value',
        ),
        migrations.AddField(
            model_name='patient_detail',
            name='doctor',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
