import csv 

name = input("what is your name? ")
home = input("where is your house? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name":name, "home": home})