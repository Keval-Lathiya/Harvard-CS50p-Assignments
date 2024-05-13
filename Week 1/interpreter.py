
user_input = input("Please enter an arithmetic expression: ")
x, y, z = user_input.split()
x, z = int(x), int(z)

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

print("{:.1f}".format(result))




