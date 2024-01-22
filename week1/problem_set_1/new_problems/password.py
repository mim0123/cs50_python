# Password Strength Checker

password = float(input("Create password: "))

if len(password) > 8:
    print("Strength = Weak")
elif  8 <= len(password) <= 12:
    print("Strength = Moderate")
else: 
    print("Strength = Strong")

