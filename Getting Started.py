# Create empty list to store numbers meeting conditions
newlist = []

# Iterate through numbers from 1500 to 2700 (inclusive)
for x in range(1500, 2701):
    # Check if the number is divisible by 7 and 5 without any remainder
    if (x % 7 == 0) and (x % 5 == 0):
        # If the conditions are met, convert the number to a string and append it to the list
        newlist.append(str(x))

# Join the numbers in the list with a comma and print the result
print(','.join(newlist))







