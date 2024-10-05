from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Item
from rest_framework_simplejwt.tokens import RefreshToken

class ItemTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_item(self):
        data = {"Name": "item1", "Description": "Test item", "Quantity": 10}
        response = self.client.post(reverse('create_item'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_item(self):
        item = Item.objects.create(Name="item1", Description="Test item", Quantity=10)
        response = self.client.get(reverse('item_detail', args=[item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        item = Item.objects.create(Name="item1", Description="Test item", Quantity=10)
        data = {"Name": "item1", "Description": "Updated description", "Quantity": 20}
        response = self.client.put(reverse('item_detail', args=[item.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item(self):
        item = Item.objects.create(Name="item1", Description="Test item", Quantity=10)
        response = self.client.delete(reverse('item_detail', args=[item.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
