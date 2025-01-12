print("Hello, Welcome to the Flower Child Chatbot!")
name = input("What is your name? ")
age = input("What is your age? ")
print(f"Welcome {name} (age {age}) to Flower Child!")
orderList = []
orderDict = {"tomato" : 5.99, "chicken" : 10.99, "onion" : 3.99}
total = 0
while True:
    print("The current Menu is: ")
    for i in orderDict.keys():
        print(i)
    order = input("Please Enter Your Order (type \"done\" if finished): ")
    if (order == "done"):
        break
    elif (order in orderDict):
        total += orderDict[order]
    orderList.append(order)
    print(f"You added {order} to your cart.")
print("Your final order is: ")
for item in orderList:
    print(item)
print(f"With a total price of {total}")