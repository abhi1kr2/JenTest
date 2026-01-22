menu = {
    'Pizza':40,
    'Pasta':35,
    'Burger':60,
    'Chow':70,
    'Kofta':80,
    'Malai': 40,
    'Mitha':30,
    'Namkeen':20

}
print("welcome to MSR Restro")
print(" Pizza = 40\n Pasta = 35\n Burger = 60\n Chow = 70\n Kofta = 80\n Malai = 40\n Mitha = 30")

order_total = 0

item_1 = input("Enter the name of item you want o order = ")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Your Order item {item_1} is not available yet!")

another_order = input("do you want to add another item? (Yes/No)")

if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total = order_total+menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Your Order item {item_2} is not available yet!")

print(f"The Total Amount of Order is Pay {order_total}")