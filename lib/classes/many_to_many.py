from statistics import mean

class Coffee:
    all = []
    def __init__(self, name):
        self._name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, 'name'):
            self._name = name
        
    def orders(self):
        pass
    
    def customers(self):
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass

class Customer:
    all = []
    def __init__(self, name):
        self._name = name
        Customer.all.append(self)

    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        
    def orders(self):
        pass
    
    def coffees(self):
        pass
    
    def create_order(self, coffee, price):
        pass
    

    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all.append(self)

    @property 
    def price(self):
        return self._price 
    
    @price.setter 
    def price(self, price):
        if isinstance(price, float) and 1.0 <= price <= 10.0 and not hasattr(self, 'price'):
            self._price = price 

    @property 
    def customer(self):
        return self._customer
    
    @customer.setter 
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property 
    def coffee(self):
        return self._coffee
    
    @coffee.setter 
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee