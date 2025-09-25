## Inputs I need from user
## total rent
## number of roommates
## total food cost
## Electricity cost
## Water cost
## Internet cost

## Outputs I want to give user
## Total cost per persion
rent = float(input("Enter the room rent: "))
num_roommates = int(input("Enter the number of roommates: "))
food = float(input("Enter the total food cost: "))
electricity = float(input("Enter the electricity cost: "))
water = float(input("Enter the water cost: "))
internet = float(input("Enter the internet cost: ")) 
total_cost = rent + food + electricity + water + internet
cost_per_persion = (total_cost / num_roommates)
print("The total cost per persion is : rs", cost_per_persion)