print("Hello, Welcome to the Flower Child Chatbot!")
name = input("What is your name? ")
print(f"Welcome {name} to Flower Child!")
orderList = []
while True:
    order = input("Please Enter Your Order (type \"done\" if finished): ")
    if (order == "done"):
        break
    orderList.append(order)
    print(f"You added {order} to your cart.")
print("Your final order is: ")
for item in orderList:
    print(item)