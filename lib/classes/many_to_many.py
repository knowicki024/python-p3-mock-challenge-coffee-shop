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
        return [order for order in Order.all if order.coffee is self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        return mean([order.price for order in self.orders()])
        

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
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, new_coffee, new_price):
        return Order(self, new_coffee, new_price)
    

    
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