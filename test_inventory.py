import unittest
from inventory import Inventory
from menu import validate_menu_item
from validators import validate_quantity

class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.inventory.add_item("Kopi", 10, 3)

    def test_stock_can_be_reduced(self):
        self.assertEqual(self.inventory.change_stock("kopi", -2), 8)

    def test_stock_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            self.inventory.change_stock("Kopi", -11)

    def test_low_stock_alert(self):
        self.inventory.change_stock("Kopi", -7)
        self.assertEqual(len(self.inventory.low_stock_items()), 1)

    def test_quantity_validation(self):
        self.assertEqual(validate_quantity(4), 4)
        with self.assertRaises(ValueError):
            validate_quantity(-1)

    def test_menu_validation(self):
        self.assertEqual(validate_menu_item("Latte", 18000)["price"], 18000.0)
        with self.assertRaises(ValueError):
            validate_menu_item("Latte", 0)

if __name__ == "__main__":
    unittest.main()
