# Pizza ordering program

# Menu prices
PIZZA_LARGE_PRICE = 6.0
PIZZA_XL_PRICE = 10.0
TOPPING_PRICES = [0, 1.0, 1.75, 2.5, 3.35]
HST_RATE = 0.13

# Input
pizza_size = input("Enter pizza size (L for large, XL for extra large): ")
topping_count = int(input("Enter number of toppings (1-4): "))

# Calculation
if pizza_size.upper() == "L":
    pizza_price = PIZZA_LARGE_PRICE
elif pizza_size.upper() == "XL":
    pizza_price = PIZZA_XL_PRICE
else:
    print("Invalid pizza size entered.")
    exit()

if topping_count < 1 or topping_count > 4:
    print("Invalid number of toppings entered.")
    exit()

topping_price = TOPPING_PRICES[topping_count]
subtotal = pizza_price + topping_price
tax = subtotal * HST_RATE
total = subtotal + tax

# Output
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
