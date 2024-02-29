from Commands.abs_command import AbsCommand
from Commands.abs_order_command import AbsOrderCommand


class ShippingOrder(AbsCommand, AbsOrderCommand):
    name = "ShippingOrder"
    description = "ShippingOrder"

    def __init__(self, args):
        self._quantity = args[1]

    def execute(self):
        print("Item shipped for {} ietms(s)".format(self._quantity))