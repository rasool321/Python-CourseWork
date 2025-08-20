from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass
    
class FoodOrder(Order):
    def process_order(self):
        print("Processing Food Order: Check chef availability, estimate time, assign delivery.")

class GroceryOrder(Order):
    def process_order(self):
        print("Processing Grocery Order: Check inventory per item, bag & dispatch.")

class MedicineOrder(Order):
    def process_order(self):
        print("Processing Medicine Order: Validate prescription, assign secure courier.")

class CloudKitchenOrder(Order):
    def process_order(self):
        print("Processing Cloud Kitchen Order: Prepare dynamically, generate OTP.")

class TiffinOrder(Order):
    def process_order(self):
        print("Processing Tiffin Subscription: Schedule weekly deliveries, manage preferences.")

class PetSuppliesOrder(Order):
    def process_order(self):
        print("Processing Pet Supplies Order: Check pet product categories and ship.")

class MeatOrder(Order):
    def process_order(self):
        print("Processing Meat/Seafood Order: Confirm freshness, assign chilled delivery.")

class CakeOrder(Order):
    def process_order(self):
        print("Processing Cake Order: Custom baking, time-sensitive packaging.")

class PartyOrder(Order):
    def process_order(self):
        print("Processing Party Order: Bulk cooking, team coordination, special packaging.")

class JuiceOrder(Order):
    def process_order(self):
        print("Processing Fresh Juice Order: Immediate prep, cold packaging.")


def handle_order(order: Order):
    order.process_order()

orders = [
    FoodOrder(),
    GroceryOrder(),
    MedicineOrder(),
    CloudKitchenOrder(),
    TiffinOrder(),
    PetSuppliesOrder(),
    MeatOrder(),
    CakeOrder(),
    PartyOrder(),
    JuiceOrder()
]

for order in orders:
    handle_order(order)