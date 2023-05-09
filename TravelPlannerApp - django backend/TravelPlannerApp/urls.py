"""TravelPlannerApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from Trip.views.profile_views import RegisterView, ActivateAccountView

urlpatterns = [
    path('', include('Trip.urls'), name="trips"),
    path('__debug__/', include('debug_toolbar.urls')),

    path('admin/', admin.site.urls),
    path('openapi/', get_schema_view(title="Travel Planner App API"), name="openapi"),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'openapi'}
    ), name='swagger-ui'),

    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name="register_view"),
    path('api/register/confirm/<str:confirmation_code>/', ActivateAccountView.as_view(), name="activate_account_view",)
]
