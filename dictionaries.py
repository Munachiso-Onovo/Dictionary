groceries = {
    "banana":5,"oranges":4,"apples":8,"pears":4,"pineapples":7
}

#prints only the keys of the dictionary
print(groceries)
print(groceries.keys())

#prints only the values of the dictionary
print(groceries.values())
print(groceries.items())

for i in groceries:
    print(i)

for i in groceries:
    print(i,groceries[i])
 
print("apples" in  groceries)
print("apples" not in  groceries)

print("strawberries" in  groceries)
print("strawberries" not in  groceries)

if "apples" in groceries:
    print("It is in the groceries dictionary")

else:
    print("It is not there")

#how to extract the individual items of the key
print(groceries["banana"])

#how to change tthe value of the key
groceries["apples"] = 20
print(groceries)