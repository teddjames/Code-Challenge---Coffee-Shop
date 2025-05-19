from customer import Customer
from coffee import Coffee
from order import Order

if __name__ == "__main__":
    # Sample customers & coffees
    alice   = Customer("Alice")
    bob     = Customer("Bob")
    latte   = Coffee("Latte")
    mocha   = Coffee("Mocha")
    espresso= Coffee("Espresso")

    # Alice’s orders
    alice.create_order(latte,    4.5)
    alice.create_order(latte,    5.0)
    alice.create_order(espresso, 6.0)

    # Bob’s orders
    bob.create_order(latte, 10.0)
    bob.create_order(mocha,  7.5)

    # Verify relationships
    print("Alice’s Orders:",    alice.orders())
    print("Alice’s Coffees:",   alice.coffees())
    print("Latte Orders:",      latte.orders())
    print("Latte Customers:",   latte.customers())

    # Aggregates
    print("Latte Num Orders:",      latte.num_orders())
    print("Latte Average Price:",   latte.average_price())

    # Bonus
    print("Top Aficionado for Latte:", Customer.most_aficionado(latte))
