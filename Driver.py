from Module import Module

def shoppingCart():
    list = []
    userchoice = int(input("How many items will you order today? "))
    if userchoice < 1:
       print("Number of items must be at least 1")
       
    else:
       for n in range(userchoice):
          while True:
             food = (str(input("Enter food: ")))
             amount = (float(input(f"Enter the amount in pounds: ")))

             order = (food, amount)
             list.append(order)

    return list

def display_list(order):
   for order in order:
      print(order)

def totalPrice(order):
    total_cost = 0.0
    for order in order:
        total_cost += order.totalPrice()
    return total_cost

def main():
   order = shoppingCart()
   display_list(order)
   total_cost = totalPrice(order)
   print(f"\nTotal Cost of All Items: ${total_cost: .2f}")


main()



    



             
             
             