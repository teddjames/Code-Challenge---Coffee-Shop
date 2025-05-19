from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from order import Order
    from customer import Customer

class Coffee:
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        self._name = name

    @property
    def name(self) -> str:
        return self._name
    # no setter → immutable

    def orders(self) -> List['Order']:
        """All Order instances for this coffee."""
        from order import Order
        return [o for o in Order._all_orders if o.coffee is self]

    def customers(self) -> List['Customer']:
        """Unique Customer instances who have ordered this coffee."""
        from order import Order
        seen = []
        for o in Order._all_orders:
            if o.coffee is self and o.customer not in seen:
                seen.append(o.customer)
        return seen

    def num_orders(self) -> int:
        """Total number of times this coffee has been ordered."""
        return len(self.orders())

    def average_price(self) -> float:
        """
        Average price across all orders of this coffee,
        or 0.0 if there are no orders.
        """
        all_orders = self.orders()
        if not all_orders:
            return 0.0
        return sum(o.price for o in all_orders) / len(all_orders)
