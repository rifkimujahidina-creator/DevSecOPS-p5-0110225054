"""Validasi data menu kafe."""
def validate_menu_item(name, price):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Nama menu wajib diisi")
    if not isinstance(price, (int, float)) or isinstance(price, bool) or price <= 0:
        raise ValueError("Harga menu harus lebih besar dari nol")
    return {"name": name.strip(), "price": float(price)}
