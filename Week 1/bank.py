Greeting = input("Greet the customer : ").lower()

if Greeting.lstrip().startswith("hello"):
    payment = "$0"
    print(payment)
elif Greeting.lstrip().startswith("h"):
    payment = "$20"
    print(payment)
else:
    payment = "$100"
    print(payment)