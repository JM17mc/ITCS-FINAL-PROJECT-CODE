customer = input("Are you a customer? (yes/no) : ")
isBuy = input("Did you buy a grocery? (yes/no) : ")
 
if isBuy.lower() == "yes" :
     age = eval(input("Enter your age: "))
     n_item = input("Name of the item: ")
     p_item = eval(input("Enter the price of an item/s: "))
     Am_given = eval(input("Amount Given: "))
     discount = round(p_item * 0.052, 2)
     discount_p = round(p_item - discount, 2)
     tax = round(p_item * 0.123, 2)
     tax_p = round(p_item + tax)
     
     print("____________________________________________________")
     print("RECEIPT")
 
     if age >= 60:
         print(f"\nHi, our dear customer, you purchased a/an {n_item}, that costs {p_item}Php plus a 5.2% discount {discount}Php to your total purchase. ")
         print(f"\nTotal: {round(p_item - discount, 2)} ")
         print(f"Change: {round(Am_given - discount_p, 2)} ")
         print("Thank you for shopping, see you next time! ")
 
     elif age >=18:
         print(f"\nHi, our dear customer, you purchased a/an {n_item}, that costs {p_item}Php plus a 12.3% tax {tax}Php to your total purchase. ")
         print(f"\nTotal: {round(p_item + tax, 2)} ")
         print(f"Change: {round(Am_given - tax_p, 2)} ")
         print("Thank you for shopping, see you next time! ")
 
     elif age >=0:
         print(f"\nHi, our dear customer, you purchased a/an {n_item}, that costs {p_item}Php. ")
         print(f"\nTotal: {round(p_item)} ")
         print(f"Change: {round(Am_given - p_item, 2)} ")
         print(f"Thank you for shopping, see you next time! ")
 
else:
     print("\nThank you for visiting, see you next time! ")
 
 

















































