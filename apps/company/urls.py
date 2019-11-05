from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from company.views import CompanyViewSet, StateView, CityView, PostalCodeView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='companies')


urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls', namespace='blog')),

    # provide the most basic login/logout functionality
    # enable the admin interface
    path('', include(router.urls)),
    path('cities/', CityView.as_view(), name="city_list"),
    path('states/', StateView.as_view(), name="state_list"),
    path('postal_codes/', PostalCodeView.as_view(), name="postal_code_list"),
    path('api-auth/', include(
            'rest_framework.urls', namespace='rest_framework'
        )
    )
]
