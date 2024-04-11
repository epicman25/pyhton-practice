price = 50
while(price > 0):
    print("Amount Due:",price)
    input_amount = int(input("Insert Coin: "))
    if input_amount == 25 or input_amount == 10 or input_amount == 5:
        price = price - input_amount
        if price < 0:
            print("Change Owed:",abs(price))
        if price == 0:
            print("Change Owed: 0")
    else:
        pass        
