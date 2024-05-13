

due = 50
coin = ""

while due > 0:
    coin = int(input("Insert a coin: "))
    if coin != 5 and coin != 10 and coin != 25:
        print(f"Amount Due: {due}")
    elif due - coin > 0:
        due = due - coin
        print(f"Amount Due: {due}")
    else:
        due = due - coin
        print(f"Change Owed: {due * -1}")