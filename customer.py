from typing import List, Optional, ClassVar, TYPE_CHECKING

if TYPE_CHECKING:
    # only for type checkers, avoids runtime circular import
    from order import Order
    from coffee import Coffee

class Customer:
    _instances: ClassVar[List['Customer']] = []

    def __init__(self, name: str):
        self.name = name
        Customer._instances.append(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be 1 to 15 characters long")
        self._name = value

    def orders(self) -> List['Order']:
        """All Order instances placed by this customer."""
        from order import Order
        return [o for o in Order._all_orders if o.customer is self]

    def coffees(self) -> List['Coffee']:
        """Unique Coffee instances this customer has ordered."""
        from order import Order
        from coffee import Coffee
        seen = []
        for o in Order._all_orders:
            if o.customer is self and o.coffee not in seen:
                seen.append(o.coffee)
        return seen

    def create_order(self, coffee: 'Coffee', price: float) -> 'Order':
        """Place a new order for this customer."""
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee: 'Coffee') -> Optional['Customer']:
        """
        Return the customer who has spent the most on the given coffee.
        If no orders exist for that coffee, returns None.
        """
        from order import Order
        totals = {}
        for o in Order._all_orders:
            if o.coffee is coffee:
                totals.setdefault(o.customer, 0.0)
                totals[o.customer] += o.price
        if not totals:
            return None
        return max(totals.items(), key=lambda kv: kv[1])[0]
