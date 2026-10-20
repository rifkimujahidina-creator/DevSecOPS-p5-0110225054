"""Penyajian laporan stok untuk terminal."""
def format_inventory_report(items):
    if not items:
        return "Belum ada bahan baku."
    lines = ["Bahan | Stok | Minimum | Status"]
    for item in items:
        status = "PERLU RESTOCK" if item["quantity"] <= item["minimum_stock"] else "Aman"
        lines.append(
            f'{item["name"]} | {item["quantity"]} | '
            f'{item["minimum_stock"]} | {status}'
        )
    return "\n".join(lines)
