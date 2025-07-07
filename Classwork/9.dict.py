#initialized empty dict
s ={}
print(s)#{}
s1=dict()
print(s1)#{}

s = {"name": "rasool","age": 21,"course": "DS"}
print(s) #{'name': 'rasool', 'age': 21, 'course': 'DS'}

#accesing values
print(s["name"]) # Output: Alice
print(s.get("age")) # Output: 21
print(s.get("branch", "NotAvailable")) # Output: NotAvailable

#adding and updating ele
s["age"] = 22 # Updating existing key
s["city"] = "New York" # Adding a new key-value pair
print(s) #{'name': 'Alice', 'age': 22, 'course': 'Computer Science','city': 'New York'}

#removing ele
age = s.pop("age")
print(age) # Output: 22
print(s) #{'name': 'rasool', 'course': 'DS', 'city': 'New York'}
#del
del s["course"]
print(s)#{'name': 'rasool', 'city': 'New York'}
#popitem
s.popitem() #popitem last ele
print(s)#{'name': 'rasool'}
#clear
s.clear()
print(s) #{}

s = {"name": "rasool","age": 21,"course": "DS"}
print(s.keys())#dict_keys(['name', 'age', 'course'])
print(s.values())#dict_values(['rasool', 21, 'DS'])
print(s.items())#dict_items([('name', 'rasool'), ('age', 21), ('course', 'DS')])
s.update({"city":"New York"}) #updating
print(s) #{'name': 'rasool', 'age': 21, 'course': 'DS', 'city': 'New York'}
s.setdefault("c", "Unknown") #it sets defalut value if the key is not present
print(s) #{'name': 'rasool', 'age': 21, 'course': 'DS', 'city': 'New York', 'c': 'Unknown'}

#built in functionsin dict
print(len(s)) #5
print(min(s)) #age
print(max(s)) #name
print(sorted(s)) #['age', 'c', 'city', 'course', 'name']

students = {
"Alice": {"age": 21, "course": "CS"},
"Bob": {"age": 22, "course": "Math"}
}
print(students["Alice"]["course"]) # Output: CS