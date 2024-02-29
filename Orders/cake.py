from Commands.abs_command import AbsCommand
from Commands.abs_order_command import AbsOrderCommand


class CakeOrder(AbsCommand, AbsOrderCommand):
    name = "CakeOrder"
    description = "CakeOrder"

    def __init__(self, args):
        self._quantity = args[1]

    def execute(self):
        print("CakeOrder for {} ietms(s)".format(self._quantity))