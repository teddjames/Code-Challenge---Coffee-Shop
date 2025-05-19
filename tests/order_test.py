import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_validation():
    c = Customer("Nina")
    coffee = Coffee("Americano")
    with pytest.raises(TypeError):
        Order("not a customer", coffee, 4.0)
    with pytest.raises(TypeError):
        Order(c, "not a coffee", 4.0)
    with pytest.raises(TypeError):
        Order(c, coffee, "4.0")
    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(c, coffee, 12.0)

def test_order_creation_and_attributes():
    customer = Customer("Liam")
    coffee = Coffee("Macchiato")
    order = Order(customer, coffee, 4.0)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.0
