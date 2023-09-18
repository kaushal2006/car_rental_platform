import car
import customer

# creating list
customers = []

# appending instances to list
cust1 =Customer(101, "Kaushal Patel", "PA43331232")
customers.append(cust1)

# appending instances to list
cust2 =Customer(102, "Amy Wang", "AR43331232")
customers.append(cust2)

# appending instances to list
cust3 =Customer(102, "John Doe", "FL43331232")
customers.append(cust3)

# Accessing object value using a for loop
for cust in customers:
    print(cust)