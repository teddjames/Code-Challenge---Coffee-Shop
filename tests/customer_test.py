import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("A" * 16)

def test_customer_create_order():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 4.0)
    assert isinstance(order, Order)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.0

def test_customer_orders_and_coffees():
    customer = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Mocha")
    customer.create_order(coffee1, 4.0)
    customer.create_order(coffee2, 5.0)
    customer.create_order(coffee1, 3.5)

    assert len(customer.orders()) == 3
    assert set(customer.coffees()) == {coffee1, coffee2}

def test_most_aficionado():
    coffee = Coffee("Espresso")
    c1 = Customer("Eve")
    c2 = Customer("Max")

    c1.create_order(coffee, 2.0)
    c1.create_order(coffee, 3.0)
    c2.create_order(coffee, 6.0)

    assert Customer.most_aficionado(coffee) == c2
