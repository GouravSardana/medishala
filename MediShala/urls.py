"""MediShala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from home import views
from home.views import Home, SignUp, Patient_details, View_Patient, Request, Hosp_view_blood

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', views.user_login, name='user_login'),
    path('accounts/login/', views.user_login, name='user_login'),
    path('request_button', Request.as_view(), name='request_button'),
    path('bloodsample/', Patient_details.as_view(), name='patient_details'),
    path('hosp_view_patient/', Hosp_view_blood.as_view(), name='hosp_view'),
    path('logout/', views.user_logout, name='logout'),
    path('view_patient/', View_Patient.as_view(), name='patient'),
]

