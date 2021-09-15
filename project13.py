import math
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
bank = 0
supflag = True
clst = ["espresso","latte","cappuccino"]
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
sum1 = 0
rlst = ["water","milk","coffee"]
while supflag:
    inflag = True
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice in clst:
        mdic = MENU[choice]
        indic = mdic["ingredients"]
        cost = mdic["cost"]
        for i in rlst:
            try:
                k = resources[i]
                k = k - indic[i]
                if k < 0:
                    print("Not sufficient",i,"is available.")
                    inflag = False
                    break
            except:
                pass

        if inflag:
            qm = int(input("How many quarters you wanna input: "))
            dm = int(input("How many dimes you wanna input: "))
            nm = int(input("How many nickles you wanna input: "))
            pm = int(input("How many pennies you wanna input: "))
            sum1 = qm*quarters + dm*dimes + nm*nickles + pm*pennies
            if sum1 >= cost:
                print("Here is your money back",round((sum1-cost),2),"$")
                print("Here is your",choice)
            else:
                print("Not sufficient ammount of coins were given")
                print("Here is your refund",round(sum1,2))
                inflag = False
        if inflag:
            bank += sum1
            for i in rlst:
                try:
                    k = resources[i]
                    k = k - indic[i]
                    resources[i] = k
                except:
                    pass
    elif choice == "report":
        try:
            for i in rlst:
                print(i,":",resources[i])
        except:
            pass
        print("Money:",bank,"$")
    elif choice == "off":
        supflag = False
    else:
        print("Enter proper input!")


