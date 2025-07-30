products_data = [
{"name": "Laptop", "price": 1000, "stock": 3},
{"name": "Phone", "price": 800, "stock": 0},
{"name": "Tablet", "price": 450, "stock": 5}
]
available_names = [p["name"] for p in products_data if
p["stock"] > 0]
print(available_names)