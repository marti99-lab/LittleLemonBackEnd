from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuViewTest(APITestCase):
    def setUp(self):
        MenuItem.objects.create(title="Test Menu 1", price=10, inventory=5)
        MenuItem.objects.create(title="Test Menu 2", price=15, inventory=10)
        MenuItem.objects.create(title="Test Menu 3", price=20, inventory=7)

    def test_get_all_menu_items(self):
        url = reverse('menu-items')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = MenuItemSerializer(MenuItem.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data)