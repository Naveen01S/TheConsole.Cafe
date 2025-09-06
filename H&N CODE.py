# H&N Cafe Management System

menu = {
    "Pizza": 120,
    "Burgers": 60,
    "Pasta": 90,
    "Coffee": 20,
    "Desserts": 50,
    "Salads": 60
}

print("Welcome to the H&N Cafe ")
print("==========================")

print("Here is our menu for today:")
print("---------- Menu ----------")

for item, price in menu.items():
    print(f"{item}: Rs-{price}")
    
print("--------------------------\n")

order_total = 0
print("Let's get your order started.")

while True:

    item = input("Please select an item (or type 'done' to finish): ")

    if item.lower() == 'done':
        break 

    if item in menu:
        order_total += menu[item]
        print(f"Added '{item}' to your order.")
        print(f"Current total: Rs-{order_total}")
    else:
        print(f" Sorry, we don't have '{item}' on the menu. Please try again.")
    
    print()


print("\n==========================")
print("Thank you for your order!")
print(f"Your final total is Rs-{order_total}. ")
print("Have a great day!")