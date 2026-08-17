
username = input("Enter the username: ")
password = input("Enter the password: ")
if username == "admin" and password == "admin123":
    print("login successfuly")
else:
    print("invalid ")
   

products = ["Laptop","mobile","bag","bottel"]
search = input("search product: ")
if search in products:
    print("product Found")
else:
    print("product Not found")
   
order_bill=int(input("enter the bill: "))
if order_bill>=99:
    final_bill =order_bill
else:
    final_bill=order_bill+30
print("Final Bill Amount:",final_bill)
