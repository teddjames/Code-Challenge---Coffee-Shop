import pytest
from customer import Customer
from coffee import Coffee

def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("A")

def test_coffee_orders_and_customers():
    coffee = Coffee("Cappuccino")
    c1 = Customer("Anna")
    c2 = Customer("Tom")
    c1.create_order(coffee, 4.5)
    c2.create_order(coffee, 5.0)
    c1.create_order(coffee, 4.0)

    assert len(coffee.orders()) == 3
    assert set(coffee.customers()) == {c1, c2}

def test_num_orders_and_average_price():
    coffee = Coffee("Flat White")
    c1 = Customer("Jack")
    c1.create_order(coffee, 3.0)
    c1.create_order(coffee, 5.0)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 4.0
