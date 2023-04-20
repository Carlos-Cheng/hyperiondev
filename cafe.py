#This is a program to simulate a cafe
#Define variables
menu = ["americano", "black coffee", "cappuccino", "doppio"]
stock = {"americano":15, "black coffee":10, "cappuccino":12, "doppio":4}
price = {"americano":5, "black coffee":3, "cappuccino":4, "doppio":2}
total_stock = 0

#Loop item value for each item
for item in menu:
    item_value = (stock[item]*price[item])
    total_stock += item_value

print(total_stock) # Display total stock value

#End of program