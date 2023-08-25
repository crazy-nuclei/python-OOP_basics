from item import Item
from phone import Phone


item = Item('Aa', 2, 1)
item.send_email()



"""
Price cannot be directly accessed in phone class methods 
phone = Phone("A", 10, 10, 1)
#phone.increase(20)

print(phone.price)
print(phone.name)
"""



"""
Price is now read only attribute

item = Item("Aa", 100, 100)
item.apply_discount()
item.increment_price(.2)

print(item.price)"""


"""
GETTERS AND SETTERS FOR ENCAPSULATION 

item = Item("AA", 1, 1)
item.name =  "BBB"
print(item.name)"""

"""
check the all (class attribute) using Phone class
phone = Phone("A", 1, 1, 1)
item = Item("B", 2, 2)
print(Phone.all)"""

"""
Check if the number is an integer using a static method 
print(Item.is_integer(7.00))
"""

"""
Initiate objects from a csv file

Item.instantiate_from_csv()
print(Item.all)
"""

"""
Changing the representation 

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)"""


"""
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

if we want to have different pay_rate for specific products
"""


"""
How to check class level and instance level variables

print(Item.__dict__)
print(item.__dict__)

"""