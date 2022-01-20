postalCode = input("Enter your Postal Code: ")
newPostalCode = postalCode[0].upper() + postalCode[1].upper()
for i in range(2, len(postalCode)):
    print(postalCode[i].lower())

print(postalCode)
print(newPostalCode)