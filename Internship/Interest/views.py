from django.shortcuts import reverse, redirect
from django.http import HttpResponseForbidden

# Generic View
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

# Pagination
from django.core.paginator import Paginator
# Rest API
from .serializer import InterestCompanySerializer

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import InterestCompany
from .forms import InterestCompanyForm
from .process import get_internship_information
# Create your views here.


class InterestCompanyViewSet(viewsets.ModelViewSet):
    queryset = InterestCompany.objects.all()
    serializer_class = InterestCompanySerializer

    @action(detail=False, methods=['post'])
    def create_interestcompany(self, request):
        serializer = InterestCompanySerializer(data=request.data)
        if serializer.is_valid():
            InterestCompany.objects.create(
                user=serializer.validated_data['user'],
                company_name=serializer.validated_data['company_name'],
                intern_title=serializer.validated_data['intern_title'],
                duration=serializer.validated_data['duration']
            )
            return Response({'status': 'create interestcompany'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


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

    def get_queryset(self):
        if self.request.user.is_anonymous: # 로그인되지 않은 경우
            return []
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(InterestCompanyListView, self).get_context_data(**kwargs)
        internship_info = get_internship_information()
        page = self.get_page_number()
        total_page_list = Paginator(internship_info, 12)
        curr_page = total_page_list.get_page(page)
        context['internship_information'] = internship_info
        context['internship_obj'] = curr_page
        return context


class InterestCompanyCreateView(LoginRequiredMixin, CreateView):
    model = InterestCompany
    form_class = InterestCompanyForm
    template_name = 'Interest/interestcompany_create.html'
    login_url = 'common-login'

    def get_success_url(self):
        return reverse('company-list')

    def form_valid(self, form):
        form.instance.user = self.request.user # user 객체 추가
        return super().form_valid(form)


class InterestCompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = InterestCompany
    pk_url_kwarg = 'company_id'
    template_name = 'Interest/interestcompany_delete.html'
    context_object_name = 'company'
    login_url = 'common-login'

    def post(self, request, *args, **kwargs):
        # 유저가 아니라면 Forbidden
        if request.user != self.get_object().user:
            return HttpResponseForbidden()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('company-list')


class InterestCompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = InterestCompany
    form_class = InterestCompanyForm
    template_name = 'Interest/interestcompany_create.html'
    pk_url_kwarg = 'company_id'
    login_url = 'common-login'

    def post(self, request, *args, **kwargs):
        if request.user != self.get_object().user: # User이 아니라면 Forbidden
            return HttpResponseForbidden()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('company-list')


@login_required(login_url='common-login')
def InterestCompanyAllDelete(request):
    object = InterestCompany.objects.filter(user=request.user)
    object.delete()
    return redirect('company-list')






