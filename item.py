import csv

class Item: 
    pay_rate = 0.8  # Price after 20% discount
    all = []        # all the items that are present
    def __init__(self, name : str, price : float, quantity = 0):

        # Run validations on received arguments
        assert price >= 0, "Price is not greater than or equal to 0 !"
        assert quantity >= 0, "Quantity is not greater than or equal to 0 !"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute 
        Item.all.append(self)

    @property
    # Property Decorator -- read only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if(len(value) > 9):
            raise Exception("Value is too long for the name attribute")
        else: 
            self.__name = value

    @property
    def price(self):
        return self.__price

    def apply_discount(self): 
        self.__price = self.__price * self.pay_rate

    def increment_price(self, increment):
        self.__price = self.__price + self.__price*increment
    
    def calculate_total_price(self): 
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
            for item in items : 
                Item(
                    name= item.get('name'),
                    price= float(item.get('price')),
                    quantity= int(item.get('quantity'))
                )
    
    @staticmethod
    def is_integer(num): 
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else : 
            return False
        
    def __connect(self):
        pass

    def __prepare_body(self):
        pass

    def __send(self): 
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
