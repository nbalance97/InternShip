from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class InterestCompany(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # User 삭제시 관련 데이터들도 삭제되게끔.
    company_name = models.CharField(max_length=100)
    intern_title = models.CharField(max_length=100)
    duration = models.DateTimeField()
