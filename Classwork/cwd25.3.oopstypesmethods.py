'''
Shopping cart 
'''
class Shopping:
    discount=10
    cat=['men','women','footware','electronics']
    def placeorder(self,product):
        self.product=product
        print("order is placed")
        @classmethod
        def updatediscount(cls,upd_dis):
            cls.discount=upd_dis
    
            print("discount is updated")

        @staticmethod
        def formatdiscount(discount):
            print(f"{discount}%discount is availble.shop now!!!")
            
        
kowshik=Shopping()

kowshik.placeorder("phone")


kowshik.updatediscount(15)

