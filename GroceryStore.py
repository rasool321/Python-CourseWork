print("Grocery Store".center(80,'-'))
data={
    1:{'Product': 'Rice','price':60},
    2:{'Product': 'Wheat Flour','price':45},
    3:{'Product': 'Sugar','price':40},
    4:{'Product': 'Milk','price':25},
    5:{'Product': 'Eggs (12 pcs)','price':70},
    6:{'Product': 'Cooking Oil','price':130},
    7:{'Product': 'Tea Powder','price':90},
    9:{'Product': 'Salt','price':20},
    10:{'Product': 'Bread','price':30},
    11:{'Product': 'Soap','price':25}
}
for i in data :
    print(f'{i}. {data[i]["Product"]} - ${data[i]["price"]}')

l = list(map(int,input("Enter the product you want to buy (you can repeat indexes):\nEnter indexes (e.g. 1 2 2 5) :").split(',')))
print(l)
print("Your Bill".center(80,'-'))
total=0
s=set()
for i in l:
    if i not in s:
        c=l.count(i)
        print(f'{i}. {data[i]["Product"]} - {c} * ${data[i]["price"]} = {c*data[i]["price"]}')
        total += c*data[i]['price']
        s.add(i)
print(f"Total bills: {total}")
print("Thank you for shopping with us!!")


#Dynamic approach:
total =0 
while True:
    product_name = input("Enter the product name{0-Exit}:")
    if product_name == '0':
        print("Thank u ")
        break
    quantity = int(input("Enter the quantity:"))
    price = int(input("Enter the price:"))
    total += price*quantity
print(f'Total: {total}')
