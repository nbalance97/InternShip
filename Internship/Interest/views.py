from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import InterestCompany
from .forms import InterestCompanyForm
from .process import get_internship_information

# Create your views here.


class InterestCompanyListView(ListView):
    model = InterestCompany
    template_name = 'Interest/interestcompany_list.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super(InterestCompanyListView, self).get_context_data(**kwargs)
        context['internship_information'] = get_internship_information()
        return context


class InterestCompanyCreateView(CreateView):
    model = InterestCompany
    form_class = InterestCompanyForm
    template_name = 'Interest/interestcompany_create.html'

    def get_success_url(self):
        return reverse('company-list')


class InterestCompanyDeleteView(DeleteView):
    model = InterestCompany
    pk_url_kwarg = 'company_id'
    template_name = 'Interest/interestcompany_delete.html'
    context_object_name = 'company'

    def get_success_url(self):
        return reverse('company-list')


class InterestCompanyUpdateView(UpdateView):
    model = InterestCompany
    form_class = InterestCompanyForm
    template_name = 'Interest/interestcompany_create.html'
    pk_url_kwarg = 'company_id'
    
    def get_success_url(self):
        return reverse('company-list')





