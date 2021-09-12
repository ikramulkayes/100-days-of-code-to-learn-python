dic = {}
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
while True:
    name = input("Enter the bidders name: ")
    price = int(input("Enter your bid: "))
    con = input("Are there any more bidders? ")
    dic[name] = price
    if con == "no":
        break
lst = []
for k,v in dic.items():
    m = (v,k)
    lst.append(m)
lst.sort()
print("The winner is",lst[-1][1],"and his bid is",lst[-1][0])
    