#Jaqueline Chavez
#TryMoreTreats Ver 1
#Date: 11/20/2022

itemNumber = 1
itemNumber = 2
itemNumber = 3
itemNumber = 4
#Prompt will ask the user to input how many items the customer ordered
itemNumber = int(input("Enter the number of items the customer ordered:"))
#Prompt will ask the user to input the price for each item by using an array to input the price depending on 
#how many items the customer ordered
print('Enter the price of each item:')
arr = []
price = []
#The following shows the discount break down depending on how many items were ordered
for i in range(itemNumber):
    itemPrice = float(input())
    arr.append(itemPrice)
if itemNumber == 1:
    discount = 0
elif itemNumber == 2:
    discount = 0.10
elif itemNumber == 3:
    discount = 0.15
elif itemNumber == 4:
    discount = 0.20
else:
    discount = 0.20
    print('20% coupon for an item in their next purchase at a later date')
#This calculates the final price of each item based on the inputs of how many items were ordered and the applied discount
for i in range(itemNumber):
    discountPrice = (arr[i]-arr[i]*discount)
    price.append(discountPrice)
#After the calculation, the final price of each item is displayed 
print(price)
