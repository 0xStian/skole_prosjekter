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

def calculate(choice, type, pizza_sum):
    if choice in type:
        print(f"you chose ({choice})")
        pizza_sum += type[choice]
        return pizza_sum
    else:
        print(f"{choice} is not in {type}. Start over!")
        quit()
        
def topping():
    temp_sum = 0
    pizza_topping_choice = []
    print("# Choose multiple toppings, if you are done or dont want toppings, type 'done'")
    while True:
        temporary_choice = input("pizza_topping (cheese, mushrooms, avocado, pineapple, bacon, chicken, fish): ").lower()
        if temporary_choice != "done":
            pizza_topping_choice.append(temporary_choice)
            print(f"you chose {pizza_topping_choice}")
        elif temporary_choice == "done":
            for x in pizza_topping_choice:
                if x in pizza_topping:
                    temp_sum += pizza_topping[x]
            return temp_sum

base_sum = calculate(input("pizza_base (thick, thin): ").lower(), pizza_base, pizza_sum)
size_sum = calculate(input("pizza_size (small, medium, large): ").lower(), pizza_size, pizza_sum)
sauce_sum = calculate(input("pizza_sauce (tomato, barbecue): ").lower(), pizza_sauce, pizza_sum)
topping_sum = topping()

print(f"Pizza sum = {base_sum + size_sum + sauce_sum + topping_sum}")
