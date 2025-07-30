products_colors = [
{"name": "Laptop", "colors": ["Silver", "Black"]},
{"name": "Phone", "colors": ["Gold", "Blue"]}
]
all_colors = [color for product in products_colors for color
in product["colors"]]
print(all_colors)