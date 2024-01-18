greet = input("Greeting: ")
if greet.strip().startswith("Hello"):
    print("$0")
elif greet.strip().startswith("hello"):
    print("$0")
elif greet.strip().startswith("H") or greet.strip().startswith("h"):
    print("$20")
else:
    print("$100")