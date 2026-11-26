# membership operators

"""
registered = ["Ali","Rahul","sara"]

print("Ali" in registered)
print("Aman" not in registered)
"""

# in - operator
# data collection - particlualr value present hai - True
# Not present - False


# for loops 

"""
registered = ["Ali","Rahul","sara"]
participants = ["Ali", "Aman","sara"]

for name in participants:
    if name in registered:
        print(name,"Is Registered")


"""




# Example -1 

"""
shopping = ["milk","bread","eggs","butter"]

print("bread" in shopping)
print("chocolate" in shopping)
"""

# not in - Not present
# present nahi hai - True
# present - False

# Example - 1
"""
employees = ["Ali","Rahul","Sara"]

print("Aman" not in employees)
print("Ali" not in employees)
"""

"""
registered = ["Ali","Rahul","sara"]
participants = ["Ali", "Aman","sara"]

for name in participants:
    if name not in registered:
        print(name,"Is Not Registered")
"""


# question 

customer_ids = [101,102,103,101,102,105]
output = [101,102,103,105]

unique =[]

for ids in customer_ids:
    if ids not in unique:
        unique.append(ids)
print(unique)


"""
Use for loop 
Use the (in) operator
dont use set()
Store unique elements in a new list
unique =[]
"""
