from django.forms import ModelForm, TextInput
from .models import InterestCompany

class InterestCompanyForm(ModelForm):
    class Meta:
        model = InterestCompany
        fields = ['company_name', 'intern_title', 'duration'] # __all__로 치환 가능
        widgets = {
            'company_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'intern_title': TextInput(attrs={
                'class': 'form-control'
            }),
            'duration': TextInput(attrs={
                'class': 'form-control'
            }),
        }