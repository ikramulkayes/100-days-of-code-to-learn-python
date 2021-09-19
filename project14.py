from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money = MoneyMachine()
coffe_menu = Menu()
flag = True
resource = CoffeeMaker()

while flag:
    choice = input("What coffe would you like"+coffe_menu.get_items())
    if choice == "off":
        flag = False
    elif choice == "report":
        money.report()
        resource.report()
    else:
        menu = coffe_menu.find_drink(choice)
        flag1 = resource.is_resource_sufficient(menu)
        #print(flag1)
        if flag1:
            cost = money.make_payment(menu.cost)
            if cost:
                resource.make_coffee(menu)
            


