from django.test import TestCase
from django.urls import reverse
from company.models import City, State, Company
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
# Create your tests here.


class APITests(APITestCase):
    def setUp(self):
        state = State()
        state.name = 'Anhui'
        state.save()

        city = City()
        city.name = 'Anqing'
        city.state = state
        city.save()

        company = Company()
        company.name = 'Sinotech'
        company.city = city
        company.state = state
        company.locality = "Hunnan Qu"
        company.building_number = "12122"
        company.postal_code = "12111"
        company.save()
        self.state = state
        self.city = city
        

    def test_get_all_cities(self):
        """
        Ensure we can get all cities.
        """
        url = reverse('city_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert isinstance(response.data, list)

    def test_get_all_states(self):
        """
        Ensure we can get all states.
        """
        url = reverse('state_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert isinstance(response.data, list)

    def test_company_crud(self):
        """
        Ensure company CRUD works
        """
        url = reverse('companies-list')
        response = self.client.post(
            url, 
            data={
                'name': 'ChangHong', 
                'city': self.city.pk, 
                'state': self.state.pk, 
                'locality': 'Beinan Lu',
                'building_number': '11211',
                'postal_code': '12111'
            }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        company = response.data

        url = reverse('companies-detail', args=[company.get('id')])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(company, response.data)


    def test_get_companies_with_city(self):
        """
        Ensure we can get all companies from city id
        """
        url = reverse('companies-list')
        response = self.client.get(url, data={"city_id": self.city.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert isinstance(response.data, list)
        
    def test_get_company_with_name(self):
        """
        Ensure we can get company with name
        """
        url = reverse('companies-list')
        response = self.client.get(url, data={"name": "ChangHong"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert isinstance(response.data, list)

    def test_get_postal_codes_with_x_company(self):
        """
        Ensure we can get postal_code with more than x companies in it
        """
        url = reverse('postal_code_list')
        response = self.client.get(url, data={"num_companies": 1}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        assert isinstance(response.data, list)
