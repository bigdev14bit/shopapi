from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Category, Product


class CatalogModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Books",
            slug="books",
            description="Printed and digital books.",
        )

    def test_category_string_and_product_relation(self):
        product = Product.objects.create(
            category=self.category,
            name="Django Guide",
            slug="django-guide",
            description="A guide to Django.",
            price=Decimal("24.99"),
        )

        self.assertEqual(str(self.category), "Books")
        self.assertEqual(str(product), "Django Guide")
        self.assertEqual(list(self.category.products.all()), [product])
        self.assertEqual(product.price, Decimal("24.99"))

    def test_product_price_cannot_be_negative(self):
        product = Product(
            category=self.category,
            name="Invalid Product",
            slug="invalid-product",
            price=Decimal("-0.01"),
        )

        with self.assertRaises(ValidationError):
            product.full_clean()
