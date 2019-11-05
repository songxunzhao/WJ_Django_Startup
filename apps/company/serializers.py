from rest_framework import serializers
from company.models import Company, City, State


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ['id']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        read_only_fields = ['id']


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
        read_only_fields = ['id']

class PostalcodeSerializer(serializers.Serializer):
    postal_code = serializers.CharField(max_length=255, read_only=True)
    num_companies = serializers.IntegerField(read_only=True)
