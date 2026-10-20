"""Validasi input stok dan kuantitas."""
def validate_quantity(value):
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("Kuantitas harus bilangan bulat nonnegatif")
    return value
