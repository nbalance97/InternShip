
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import signup
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name="common-login"),
    path('logout/', auth_views.LogoutView.as_view(), name="common-logout"),
    path('signup/', signup, name="common-signup")
]
