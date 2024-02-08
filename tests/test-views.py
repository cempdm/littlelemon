from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.views import ModelViewSet, MenuItemView
from rest_framework.test import APIClient

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.menu1 = MenuItem.objects.create(name="Pizza", price=12)
        self.menu2 = MenuItem.objects.create(name="Pasta", price=10)
    
    def test_getall(self):
        url = '/your-api-endpoint/'
        response = self.client.get(url)
        # Assert successful response
        self.assertEqual(response.status_code, 200)

        expected_data = [
            {"id": self.menu1.id, "name": "Pizza", "price":12},
            {"id": self.menu2.id, "name": "Pasta", "price":10}
        ]
        self.assertEqual(response.data, expected_data)
