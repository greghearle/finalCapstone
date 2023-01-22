from tabulate import tabulate # importing tabulate in order to tabulate data later on
#========The beginning of the class==========
class Shoe: # defining Shoe class

    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}" # Prints the object as a string in the same format as the inventory file

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list=[] # empty list!
#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as f: # read only
            next(f)
            for line in f:
                line_split = line.strip().split(",") # splits each line into an indexable list
                shoe = Shoe(line_split[0],line_split[1],line_split[2],line_split[3],line_split[4]) # uses the indexes as arguments for creating a shoe object
                shoe_list.append(shoe) # appends the shoe to the list
    except Exception: # exception handling message
        print("Oops! That didn't work. Please check you have a valid inventory file at 'inventory.txt'")

def capture_shoes():
    read_shoes_data() # calls the function to populate the shoe_list
    country = input("Please enter the country where these shoes are located") # asking for each detail for the argument
    code = input("Please enter the code for these shoes")
    product = input("Please enter the product name for these shoes")
    try:
        cost = int(input("Please enter the cost for these shoes"))
    except Exception: # exception handling message in case input isn't a valid number
        print("Oops! That didn't work. Please ensure you enter a number for the cost'")
    try:
        quantity = int(input("Please input the quantity of these shoes"))
    except Exception: # exception handling message in case input isn't a valid number
        print("Oops! That didn't work. Please ensure you enter a number for the cost'")
    shoe = Shoe(country,code,product,cost,quantity) # creates shoe object
    shoe_list.append(shoe) # appends shoe to list
    with open("inventory.txt","w") as f: # opens inventory file to write
        f.write("Country,Code,Product,Cost,Quantity\n") # rewrites header line
        for i in range(0,len(shoe_list)): # rewrites entire list below
            f.write(shoe_list[i].__str__()+"\n")
    print(f"{shoe.product} succesfully added to inventory") # prints confirmation message
  
def view_all():
    read_shoes_data() # calls the function to populate the shoe_list
    line_list = [] # empty list to store the details (enables tabulation of data)
    for i in shoe_list:
        line = i.__str__() # calls each line of the list as a string
        line_list.append(line.split(",")) # splits the string into a list
    print(tabulate(line_list, headers=["Country","Code","Product","Cost","Quantity"],tablefmt="mixed_grid")) # tabulates the list, along with titled headers and some formatting

def re_stock():
    read_shoes_data() # calls the function to populate the shoe_list
    minimum_quantity = float("inf") # infinity variable to help decide the minimum value (i.e. <)
    for i in shoe_list: # goes through the shoe_list and checks to see whether the quantity is the lowest seen so far
        shoe_quantity = int(i.quantity)
        if shoe_quantity < minimum_quantity: # if the quantity is the lowest so far
            minimum_quantity = shoe_quantity # sets the current lowest as the minimim by which all future numbers should be compared
            minimum_item = i # variable to store the entire object that is linked to that minimum value
    restock_yes_no= input(f"The lowest stocked item is {minimum_item.product}: {minimum_item.quantity}; would you like to re-stock these shoes?").lower() # once minimum found, message prints to show the product and its quantity, before asking the user whether they wish to restock. lower() for case sensitivity
    if restock_yes_no == "yes":
        restock_quantity = int(input("What quantity would you like to restock this item?")) # asks user to provide a number to add on to the stock
        updated_quantity = minimum_quantity+restock_quantity # variable to store this additional value onto the original stock value
        minimum_item.quantity = updated_quantity # replaces the quantity stored in the object with the new value
        print(f"{minimum_item.product} successfully restocked. New quantity: {minimum_item.quantity}") # confirmation message
    with open("inventory.txt","w") as f: # rewrites the file to update
        f.write("Country,Code,Product,Cost,Quantity\n")
        for i in range(0,len(shoe_list)):
            f.write(shoe_list[i].__str__()+"\n")

def search_shoe():
    read_shoes_data() # calls the function to populate the shoe_list
    product_code = input("Please enter the product code").upper() # .upper() to ensure the SKU section is case-correct
    for i in shoe_list: # looks through the shoe_list
        if i.code == product_code: # if the code provided by the user matches the code part of the object
            print(i.__str__()) # prints the entire object

def value_per_item():
    read_shoes_data() # calls the function to populate the shoe_list
    grand_total = 0 # variable to store the grand_total of all items
    values_list = [] # empty list to store the relevant values to tabulate
    for i in shoe_list:
        total_value = int(i.cost)*int(i.quantity) # casts to int to ensure the multiplication works, stores the total value for an item
        values_list.append([i.product,i.cost,i.quantity,total_value]) # appends the relevant values to the list
        grand_total += total_value # adds on the total_value to the grand total
    print(tabulate(values_list,headers=["Product","Cost","Quantity",f"Total Value\n(All stock:{grand_total})"],tablefmt="mixed_grid")) # tabulates information

def highest_qty(): # very similar to re_stock function, but with lots of inverse logic!
    read_shoes_data() # calls the function to populate the shoe_list
    maximum_quantity = 0 # sets a variable to compare with values to determine the maximum
    for i in shoe_list:
        shoe_quantity = int(i.quantity) # stores the quantity of shoes as an integer
        if shoe_quantity > maximum_quantity: # compares to maximum_quantity to determine highest quantity
            maximum_quantity = shoe_quantity # stores the highest quantity found so far
            maximum_item = i # stores the object linked to maximum value
    discount_yes_no = input(f"The highest stocked item is {maximum_item.product}: {maximum_item.quantity}; this shoe should now be put on 20% discount! Reply 'Yes' to confirm").lower() # message displaying the most abundant shoe, and suggests 20% discount
    if discount_yes_no == "yes":
        maximum_item.cost = round(int(maximum_item.cost)*0.8,2) # multplies by 0.8 to do 20% discount, and round(,2) to return a valid cost
        print(f"{maximum_item.product} now on sale. New price: {maximum_item.cost}") # prints message to confirm discount
    with open("inventory.txt","w") as f: # rewrites file to update inventory.txt
        f.write("Country,Code,Product,Cost,Quantity\n")
        for i in range(0,len(shoe_list)):
            f.write(shoe_list[i].__str__()+"\n")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

menu = "" # empty variable to store menu
while menu != "Q": # while user wants to keep using the program
    menu = input('''
--------------------------------------------------
-------Welcome to the Nike Global Database!-------
----Please select one of the following options----
-------------(V) View All Stock-------------------
--------------(A) Add New Shoes-------------------
--------------(R) Restock Shoes-------------------
-------------(S) Search for Shoe------------------
------------(T)  Total Value Per Shoe-------------
-------------(D) Discount Overstock---------------
---------------(Q) Quit Program-------------------
--------------------------------------------------
''').upper()
    if menu == "V":
        shoe_list=[] # resets shoe list
        view_all() # calls view_all
        
    
    elif menu == "A":
        shoe_list=[] # resets shoe list
        capture_shoes() # calls capture_shoes
        
    
    elif menu == "R":
        shoe_list=[] # resets shoe list
        re_stock() # calls re_stock
        
    
    elif menu == "S":
        shoe_list=[] # resets shoe list
        search_shoe() # calls search_shoe
        
    
    elif menu == "T":
        shoe_list=[] # resets shoe_list
        value_per_item() # calls value_per_item
        
    
    elif menu == "D":
        shoe_list=[] # resets shoe_list
        highest_qty() # calls highest_qty
    
    elif menu =="Q": # included this here so Q doesn't call the error message below
        pass

    else:
        print("Input not recognised, please try again!") # error message for unknown inputs
        
if menu == "Q": # quits program in event of Q
    print("Thank you, good bye!")

