from Orders.cake import CakeOrder
from Orders.no_class import NoClass
from Orders.shipping import ShippingOrder


def get_commands():
    commands = (ShippingOrder,CakeOrder)

    return dict([cls.name, cls] for cls in commands)


def parse_commands(commands, args):
    command = commands.setdefault(args[0], NoClass)
    return command(args)


def main(command, val):
    my_list = [command, val]
    commands = get_commands()

    command = parse_commands(commands, my_list[0:])
    command.execute()


# test with ShippingOrder, CakeOrder or NoOrder

main("ShippingOrder", 2)

