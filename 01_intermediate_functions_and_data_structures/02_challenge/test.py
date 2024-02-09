import unittest
from apply_discount import apply_discount

class TestApplyDiscount(unittest.TestCase):
    def test_apply_discount_1(self):
        self.assertEqual(
            apply_discount([
                {"name": "Laptop", "category": "Electronics", "price": 1200},
                {"name": "Bread", "category": "Food", "price": 2},
                {"name": "Jacket", "category": "Apparel", "price": 100}
            ], 50, 10),
            [("Laptop", 1080.0), ("Jacket", 90.0)]
        )

    def test_apply_discount_2(self):
        self.assertEqual(
            apply_discount([
                {"name": "Smartphone", "category": "Electronics", "price": 800},
                {"name": "Sneakers", "category": "Footwear", "price": 120},
                {"name": "Coffee", "category": "Beverage", "price": 5}
            ], 100, 15),
            [("Smartphone", 680.0), ("Sneakers", 102.0)]
        )

if __name__ == '__main__':
    unittest.main()