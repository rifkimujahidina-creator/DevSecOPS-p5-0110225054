"""Entry point sederhana untuk Cafe Stock Manager."""
from inventory import Inventory
from reports import format_inventory_report

def main():
    inventory = Inventory()
    inventory.add_item("Kopi", 20, 5)
    inventory.add_item("Susu", 12, 4)
    inventory.add_item("Sirup", 8, 2)
    print("=== Cafe Stock Manager ===")
    print(format_inventory_report(inventory.list_items()))

if __name__ == "__main__":
    main()
