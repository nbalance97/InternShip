from rest_framework import serializers
from .models import InterestCompany


class InterestCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestCompany
        fields = "__all__"
