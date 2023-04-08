from django.test import TestCase
from games.models import Products, Category
from django.urls import reverse
from http import HTTPStatus


class GamesListTests(TestCase):
    fixtures = ['fixtures/category.json', 'fixtures/developer.json',
                'fixtures/games.json', 'fixtures/link_purchase.json',
                'fixtures/publisher.json', 'fixtures/purchaseMethod.json']

    def setUp(self):
        self.games = Products.objects.all()
        self.category = Category.objects.first()

    def test_list(self):
        path = reverse('products')
        response = self.client.get(path)

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'games/products.html')
        self.assertEquals(list(response.context_data['object_list']), list(self.games))

    def test_list_with_category(self):
        path = reverse('games:categories_products', kwargs={'category_id': self.category.id})
        response = self.client.get(path)
        self.assertTemplateUsed(response, 'games/products.html')
        self.assertEquals(list(response.context_data['object_list']),
                          list(self.games.filter(category_id=self.category.id))
                          )

