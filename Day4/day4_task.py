print("1. Electronics")
print("2. Clothing")
print("3. Grocery")
print("4. Cart")
print("5. Payment")
print("6. Exit")

choice = int(input("Select main option: "))

# Electronics
if choice == 1:
    print("\nElectronics Menu")
    print("1. Mobile Phones")
    print("2. Laptops")
    print("3. Television")
    print("4. Headphones")
    print("5. Accessories")
    print("6. Back")

    e = int(input("Select electronics item: "))

    if e == 1:
        print("Mobile Phone added to cart")
    elif e == 2:
        print("Laptop added to cart")
    elif e == 3:
        print("Television added to cart")
    elif e == 4:
        print("Headphones added to cart")
    elif e == 5:
        print("Accessories added to cart")
    elif e == 6:
        print("Going back to main menu")
    else:
        print("Invalid electronics choice")

# Clothing
elif choice == 2:
    print("\nClothing Menu")
    print("1. Men's Wear")
    print("2. Women's Wear")
    print("3. Kids Wear")
    print("4. Winter Collection")
    print("5. Summer Collection")
    print("6. Back")

    c = int(input("Select clothing item: "))

    if c == 1:
        print("Men's Wear added to cart")
    elif c == 2:
        print("Women's Wear added to cart")
    elif c == 3:
        print("Kids Wear added to cart")
    elif c == 4:
        print("Winter Collection added to cart")
    elif c == 5:
        print("Summer Collection added to cart")
    elif c == 6:
        print("Going back to main menu")
    else:
        print("Invalid clothing choice")

# Grocery
elif choice == 3:
    print("\nGrocery Menu")
    print("1. Rice & Wheat")
    print("2. Pulses")
    print("3. Vegetables")
    print("4. Fruits")
    print("5. Beverages")
    print("6. Back")

    g = int(input("Select grocery item: "))

    if g == 1:
        print("Rice & Wheat added to cart")
    elif g == 2:
        print("Pulses added to cart")
    elif g == 3:
        print("Vegetables added to cart")
    elif g == 4:
        print("Fruits added to cart")
    elif g == 5:
        print("Beverages added to cart")
    elif g == 6:
        print("Going back to main menu")
    else:
        print("Invalid grocery choice")

# Cart
elif choice == 4:
    print("\nCart Menu")
    print("1. View Cart")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Update Quantity")
    print("5. Clear Cart")
    print("6. Back")

    cart = int(input("Select cart option: "))

    if cart == 1:
        print("Displaying cart items")
    elif cart == 2:
        print("Item added to cart")
    elif cart == 3:
        print("Item removed from cart")
    elif cart == 4:
        print("Item quantity updated")
    elif cart == 5:
        print("Cart cleared")
    elif cart == 6:
        print("Going back to main menu")
    else:
        print("Invalid cart option")

# Payment
elif choice == 5:
    print("\nPayment Menu")
    print("1. Cash on Delivery")
    print("2. Credit Card")
    print("3. Debit Card")
    print("4. UPI")
    print("5. Net Banking")
    print("6. Back")

    p = int(input("Select payment method: "))

    if p == 1:
        print("Order placed with Cash on Delivery")
    elif p == 2:
        print("Payment done using Credit Card")
    elif p == 3:
        print("Payment done using Debit Card")
    elif p == 4:
        print("Payment done using UPI")
    elif p == 5:
        print("Payment done using Net Banking")
    elif p == 6:
        print("Going back to main menu")
    else:
        print("Invalid payment option")

# Exit
elif choice == 6:
    print("Thank you for shopping with us!")

else:
    print("Invalid main menu choice")
