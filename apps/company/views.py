from django.shortcuts import render
from django.db.models import Count
from company.models import Company, State, City
from company.serializers import (
    CompanySerializer, StateSerializer, CitySerializer, PostalcodeSerializer
)
from rest_framework import views, mixins, generics, viewsets


# Create your views here.
class CityView(generics.ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name is None:
            return City.objects.all()
        else:
            return City.objects.filter(name__startswith=name)


class StateView(generics.ListAPIView):
    serializer_class = StateSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name is None:
            return State.objects.all()
        else:
            return State.objects.filter(name__startswith=name)


class CompanyViewSet(viewsets.ModelViewSet):
    """
    A viewset for CRUD operation of company table
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def filter_queryset(self, queryset):
        name = self.request.query_params.get('name')
        city_id = self.request.query_params.get('city_id')

        if name is not None:
            return queryset.filter(name=name)

        if city_id is not None:
            return queryset.filter(city_id=city_id)

        return queryset


class PostalCodeView(generics.ListAPIView):
    """
    A list view to search Post code with more than X number of companies
    """
    serializer_class = PostalcodeSerializer

    def get_queryset(self):
        num_companies = self.request.query_params.get('num_companies', 0)

        return Company.objects.values('postal_code').annotate(
            num_companies=Count('id')
        ).filter(
            num_companies__gte=num_companies
        )
