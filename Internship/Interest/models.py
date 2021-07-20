from django.db import models
# Create your models here.


class InterestCompany(models.Model):
    company_name = models.CharField(max_length=100)
    intern_title = models.CharField(max_length=100)
    duration = models.DateTimeField()
