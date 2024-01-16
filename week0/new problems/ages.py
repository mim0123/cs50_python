#convert age(yrs) into months and days 

def main():
    age = float(input("Enter your age: "))
    age_months = age * 12
    age_days = age * 365
    print(age_months,"months", age_days,"days")
main()