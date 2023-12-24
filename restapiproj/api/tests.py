# Run these tests using python manage.py test in your Django project directory.
# Create your tests here.

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import fooddata


class FoodDataViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_fooddata(self):
        response = self.client.get('/api/viewall/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_fooddata(self):
        data = {
            'area_abbreviation_1': 'Test Area',
            'item_code': 6,
        }
        response = self.client.post('/api/putdata/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_fooddata(self):
        food_data = fooddata.objects.create(area_abbreviation_1='Test Area', item_code=123)
        response = self.client.get(f'/api/view/{food_data.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_fooddata(self):
        food_data = fooddata.objects.create(area_abbreviation_1='Test Area', item_code=123)
        response = self.client.delete(f'/api/delete/{food_data.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_fooddata(self):
        food_data = fooddata.objects.create(area_abbreviation_1='Test Area', item_code=123)
        data = {'item_code': 456}  # Update fields as needed
        response = self.client.patch(f'/api/update/{food_data.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_fooddata(self):
        response = self.client.get('/api/search/', {'query': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class FoodDataModelTestCase(TestCase):
    def setUp(self):
        # Set up test data
        self.fooddata_instance = fooddata(
            area_abbreviation_1='Test Area',
            area_abbreviation_2='Test Area 2',
            area_abbreviation_3='Test Area 3',
            item_code=1,
            element_code=2,
            element='Test Element',
            unit='Test Unit',
            latitude=1.0,
            longitude=2.0,
            Y1961=10.0,
            Y1962=15.0,
            # Add other fields as needed
        )
        self.fooddata_instance.save()

    def test_fooddata_model(self):
        # Retrieve the saved instance from the database
        saved_instance = fooddata.objects.get(pk=self.fooddata_instance.pk)

        # Test each field
        self.assertEqual(saved_instance.area_abbreviation_1, 'Test Area')
        self.assertEqual(saved_instance.area_abbreviation_2, 'Test Area 2')
        self.assertEqual(saved_instance.area_abbreviation_3, 'Test Area 3')
        self.assertEqual(saved_instance.item_code, 1)
        self.assertEqual(saved_instance.element_code, 2)
        self.assertEqual(saved_instance.element, 'Test Element')
        self.assertEqual(saved_instance.unit, 'Test Unit')
        self.assertEqual(saved_instance.latitude, 1.0)
        self.assertEqual(saved_instance.longitude, 2.0)
        self.assertEqual(saved_instance.Y1961, 10.0)
        self.assertEqual(saved_instance.Y1962, 15.0)
        # Add other assertions for the remaining fields

    def tearDown(self):
        # Clean up test data
        self.fooddata_instance.delete()
