# Build a program that asks the user for their age. Determine and print the ticket price. 

age = input("What's your age? ")

if age == range(0-12):
    print("Children: $5")
elif age == range(13-17):
    print("Teenager: $10")
elif age == range(18-65):
    print("Adult: $15")
else:
    print ("Senior: $12")