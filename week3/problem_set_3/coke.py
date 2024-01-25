amount_due  = 50

while amount_due > 0:
    print("Amount Due: ", amount_due)
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        amount_due -= coin 
        print (amount_due)
    else: 
        print("Cannot excpect denominations other than 5, 10, 25")
