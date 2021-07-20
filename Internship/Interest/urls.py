from django.urls import path, include
from . import views

urlpatterns = [
    path('interest/', views.InterestCompanyListView.as_view(), name='company-list'),
    path('interest/create', views.InterestCompanyCreateView.as_view(), name='company-create'),
    path('interest/<int:company_id>/delete', views.InterestCompanyDeleteView.as_view(), name='company-delete'),
    path('interest/<int:company_id>/modify', views.InterestCompanyUpdateView.as_view(), name='company-modify')
]
