#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

cust1 = Customer("Katie")
cust2 = Customer("Killian")
cust3 = Customer("Emily")

c_1 = Coffee("Cold Brew")
c_2 = Coffee("Cafe au Lait")
c_3 = Coffee("Americano")

o1 = Order(cust1, c_2, 7.6)
o2 = Order(cust3, c_1, 8.2)
o3 = Order(cust2, c_3, 9.2)

ipdb.set_trace()
