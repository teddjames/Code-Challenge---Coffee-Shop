from typing import ClassVar
from customer import Customer
from coffee import Coffee

class Order:
    _all_orders: ClassVar[list] = []

    def __init__(self, customer: Customer, coffee: Coffee, price: float):
        if not isinstance(customer, Customer):
            raise TypeError("Order.customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("Order.coffee must be a Coffee instance")
        if not isinstance(price, (int, float)):
            raise TypeError("Order.price must be a number")
        price = float(price)
        if not (1.0 <= price <= 10.0):
            raise ValueError("Order price must be between 1.0 and 10.0")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order._all_orders.append(self)

    @property
    def customer(self) -> Customer:
        return self._customer

    @property
    def coffee(self) -> Coffee:
        return self._coffee

    @property
    def price(self) -> float:
        return self._price
