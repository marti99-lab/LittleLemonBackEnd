from django.test import TestCase
from ..models import Menu
import json

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(name="Test Menu 1", price=10)
        Menu.objects.create(name="Test Menu 2", price=15)
        Menu.objects.create(name="Test Menu 3", price=20)

    def test_getall(self):
        menus = Menu.objects.all()

        serialized_data = json.dumps(list(menus.values()))

        expected_data = json.dumps([
            {"name": "Test Menu 1", "price": 10},
            {"name": "Test Menu 2", "price": 15},
            {"name": "Test Menu 3", "price": 20}
        ])

        self.assertEqual(serialized_data, expected_data)