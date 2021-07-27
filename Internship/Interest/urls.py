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
    path('interest/', views.InterestCompanyListView.as_view(), name='company-list'),
    path('interest/create', views.InterestCompanyCreateView.as_view(), name='company-create'),
    path('interest/<int:company_id>/delete', views.InterestCompanyDeleteView.as_view(), name='company-delete'),
    path('interest/deleteall', views.InterestCompanyAllDelete, name='company-all-delete'),
    path('interest/<int:company_id>/modify', views.InterestCompanyUpdateView.as_view(), name='company-modify'),
    path('interest/api/', IC_list, name="api-company-list"),
    path('interest/api/<int:pk>/', IC_detail, name="api-company-detail"),
]
