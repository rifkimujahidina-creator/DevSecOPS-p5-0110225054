"""Logika pengelolaan stok bahan baku kafe."""
class Inventory:
    def __init__(self):
        self._items = {}

    def add_item(self, name, quantity, minimum_stock=0):
        if not name or not name.strip():
            raise ValueError("Nama bahan wajib diisi")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Jumlah stok harus bilangan bulat nonnegatif")
        if not isinstance(minimum_stock, int) or minimum_stock < 0:
            raise ValueError("Batas minimum harus bilangan bulat nonnegatif")
        self._items[name.strip().lower()] = {
            "name": name.strip(), "quantity": quantity, "minimum_stock": minimum_stock
        }

    def change_stock(self, name, amount):
        key = name.strip().lower()
        if key not in self._items:
            raise KeyError(f"Bahan tidak ditemukan: {name}")
        new_quantity = self._items[key]["quantity"] + amount
        if new_quantity < 0:
            raise ValueError("Stok tidak boleh negatif")
        self._items[key]["quantity"] = new_quantity
        return new_quantity

    def list_items(self):
        return [dict(item) for item in self._items.values()]

    def low_stock_items(self):
        return [dict(item) for item in self._items.values()
                if item["quantity"] <= item["minimum_stock"]]
