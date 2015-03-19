from django.db import models


class RegistrationInformation(models.Model):
    name = models.CharField(max_length=128)
    grade = models.CharField(max_length=128)
    stu_no = models.CharField(max_length=128)
    cellphone = models.CharField(max_length=128)
