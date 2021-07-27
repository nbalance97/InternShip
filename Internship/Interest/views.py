from django.shortcuts import reverse, redirect
# Generic View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Pagination
from django.core.paginator import Paginator
# Rest API
from .serializer import InterestCompanySerializer
from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import InterestCompany
from .forms import InterestCompanyForm
from .process import get_internship_information
# Create your views here.

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request): # 실제 SessionAuthentication시 발생하는 체킹
        return  # 수행하지 않도록

class InterestCompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = InterestCompany.objects.all()
    serializer_class = InterestCompanySerializer

class InterestCompanyListView(ListView):
    model = InterestCompany
    template_name = 'Interest/interestcompany_list.html'
    context_object_name = 'objects'

    def get_page_number(self):
        page_number = self.request.GET.get('page')
        if page_number is None:
            return 1
        else:
            return page_number

    def get_context_data(self, **kwargs):
        context = super(InterestCompanyListView, self).get_context_data(**kwargs)
        internship_info = get_internship_information()
        page = self.get_page_number()
        total_page_list = Paginator(internship_info, 9)
        curr_page = total_page_list.get_page(page)
        context['internship_information'] = internship_info
        context['internship_obj'] = curr_page
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

def InterestCompanyAllDelete(request):
    object = InterestCompany.objects.all()
    object.delete()
    return redirect('company-list')






