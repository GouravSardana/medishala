from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# class Patient_Detail(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name=models.CharField(max_length=40)
#     IP=models.CharField(max_length=30)
#     gender=models.CharField(max_length=10)
#     user_email=models.CharField(max_length=40)
#     doctor=models.CharField(max_length=50)
#     hospital_value = models.CharField(max_length=50)
#     balance_due=models.IntegerField(default=0)
#     total=models.IntegerField(default=0)
#
#
#     @receiver(post_save, sender=User)
#     def update_user_profile(sender, instance, created, **kwargs):
#         try:
#             if created:
#                 Patient_Detail.objects.create(user=instance)
#             instance.profile.save()
#         except Exception as e:
#             pass
#
#     def __str__(self):
#         return self.name


class Blood_Sample(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50,blank=True, null=True)
    user_email=models.CharField(max_length=80, blank=True, null=True)
    dob=models.CharField(max_length=20, blank=True, null=True)
    blood_group=models.CharField(max_length=50, blank=True, null=True)
    hospital=models.CharField(max_length=100, blank=True, null=True)
    desc=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Request_button(models.Model):
    name=models.CharField(max_length=50,blank=True, null=True)
    blood_group=models.CharField(max_length=50, blank=True, null=True)
    dob=models.CharField(max_length=20, blank=True, null=True)
    quantity=models.CharField(max_length=100, blank=True, null=True)
    desc=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
