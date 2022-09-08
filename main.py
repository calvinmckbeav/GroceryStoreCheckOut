from items import products
from items import selected

cont = ""

# menu: dictionary -> String
# puts the available products into string format
def menu(dict):
  v = 1
  print("\n")
  print("====Welcome to Sophia's Fruit Stand!====")
  for x in dict:
    print("\t"+str(v) + ". " + x.title() + " - $" + str(dict[x]))
    v += 1

# valid_item: dictionary string -> boolean
# determines if the string is in the list
def valid_item(dict, input):
  #set default value to false
  valid = False
  
  for x in dict:
    if x.upper() == input.upper():
      valid = True
  return valid


# cart: dict, list -> String
# prints current list of items selected and the subtotal
def cart(dict, list):
  print("\nCurrent List:")
  for item in dict:
    if item in list:
      print(item.title() + " " + str(list.count(item)))
  subtotal = 0
  for purchased in list:
    subtotal += dict[purchased]
  return subtotal

(menu(products))
# main loop of the file
while cont != "no":
  item = input("Which of our delicious fresh products would you like to purchase? \n").lower()
  valid = valid_item(products, item)

  while valid== False:
    print("Sorry, I don't believe we have that item")
    item = input("Please choose another product: ").lower()
    valid = valid_item(products, item)

  count = int(input("How many would you like?"))
  for x in range(count):
    selected.append(item)
  sub = cart(products, selected)
  print("Your subtotal is $" + str(sub))

  cont = input("Would you like to continue shopping? ")

# final bill
print("\nSubtotal: $" + str(sub))
tax = 0.04 * sub
print("\ntax: $" + str(tax))
print("\nYour total comes out to $" + str(tax+sub))
print("Have a nice day!")
