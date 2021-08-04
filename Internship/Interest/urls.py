from django.urls import path, include
from . import views
from .views import InterestCompanyViewSet

IC_list = InterestCompanyViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

IC_detail = InterestCompanyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', views.InterestCompanyListView.as_view(), name='company-list'),
    path('create', views.InterestCompanyCreateView.as_view(), name='company-create'),
    path('<int:company_id>/delete', views.InterestCompanyDeleteView.as_view(), name='company-delete'),
    path('deleteall', views.InterestCompanyAllDelete, name='company-all-delete'),
    path('<int:company_id>/modify', views.InterestCompanyUpdateView.as_view(), name='company-modify'),
    path('api/', IC_list, name="api-company-list"),
    path('api/<int:pk>/', IC_detail, name="api-company-detail"),
]
