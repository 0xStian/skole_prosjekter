"""
Create a script called PizzaShop.py. A pizza shop owner has asked you to write a script that allows a customer to calculate the cost of a pizza.
He has asked you to make the following options available to the customer:

1. Pizza base (Customer must choose 1): Thick (Kr 10) or Thin (Kr 5).
2. Pizza size (Customer must choose 1): Small (Kr 30), Medium (Kr 40), or Large (Kr 50).
3. Basic sauce (Customer must choose 1): Tomato (Kr 5) or Barbecue (Kr 10).
4. Toppings (Customer may choose any or none): Cheese (Kr 5), Mushrooms (Kr 3), Avocado (Kr 7), Pineapple (Kr 5), Bacon (Kr 7), Chicken (Kr 7) or Fish (Kr 6).

If a specific item is selected, display the item and its price on the screen. At the bottom (the last line) of the display, present the customer with the purchase total.
"""

pizza_base = {"thick" : 10, "thin" : 5}
pizza_size = {"small" : 30, "medium" : 40, "large" : 50}
pizza_sauce = { "tomato" : 5, "barbecue" : 10}
pizza_topping = {"cheese" : 5, "mushrooms" : 3, "avocado" : 7, "pineapple" : 5, "bacon" : 7, "chicken" : 7, "fish" : 6}

pizza_sum = 0

pizza_base_choice = str(input("pizza_base (thick, thin): ").lower())
if pizza_base_choice in pizza_base:
    print(f"you chose ({pizza_base_choice})")
    pizza_sum += pizza_base[pizza_base_choice]

pizza_size_choice = str(input("pizza_size (small, medium, large): ").lower())
if pizza_size_choice in pizza_size:
    print(f"you chose ({pizza_size_choice})")
    pizza_sum += pizza_size[pizza_size_choice]

pizza_sauce_choice = str(input("pizza_sauce (tomato, barbecue): ").lower())
if pizza_sauce_choice in pizza_sauce:
    print(f"you chose ({pizza_sauce_choice})")
    pizza_sum += pizza_sauce[pizza_sauce_choice]



print("# Choose multiple toppings, if you dont want toppings type 'none'. if you're done type 'done'")

pizza_topping_choice = []
while True:
    temporary_choice = input("pizza_topping (cheese, mushrooms, avocado, pineapple, bacon, chicken, fish): ").lower()
    if temporary_choice != "done":
        pizza_topping_choice.append(temporary_choice)
    elif temporary_choice == "done" or "none":
        for x in pizza_topping_choice:
            print(x)
            if x in pizza_topping:
                pizza_sum += pizza_topping[x]
        print(f"Sum of pizza = {pizza_sum}kr")
        quit()

    