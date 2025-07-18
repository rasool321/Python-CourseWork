# Bike Rental Product Information System

# Collecting Product (Bike) Details
bike_id = int(input("Enter Bike ID: "))
bike_name = input("Enter Bike Model Name: ")
price = float(input("Enter Rental Price per Day (₹): "))
categories = input("Enter Bike Categories (comma-separated): ").split(",")
available_bikes_count = int(input("Enter Available Bikes: "))
rented_bikes_count = int(input("Enter Rented Bikes: "))
stock_details = (available_bikes_count, rented_bikes_count)
discount_percentage = float(input("Enter Discount Percentage: "))
features = set(input("Enter Unique Features (comma-separated): ").split(","))
supplier_name = input("Enter Rental Provider Name: ")
supplier_contact = input("Enter Provider Contact Number: ")
supplier_location = input("Enter Provider Location: ")

supplier_details = {
    "name": supplier_name,
    "contact": supplier_contact,
    "location": supplier_location
}

# Displaying the Product Details using different formatting methods.

print("\n--- Bike Rental Product Details ---\n")

print("Bike ID", bike_id)
print("Name", bike_name)
print("Rental Price:", price)
print("Bike Discount: %.2f%%" % discount_percentage)
print(f"Bike Model: {bike_name}")
print(f"Rental Price per Day: ₹{price}")
print(f"Discount Offered: {discount_percentage}%")
print(f"Available Stock: {stock_details[0]} units")
print(f"Rented Out: {stock_details[1]} units")
print("Supplier Details: Name - {}, Contact - {}, Location - {}".format(
    supplier_details['name'], supplier_details['contact'], supplier_details['location']
))
print("\nCategories:", categories)
print("Features:", features)
