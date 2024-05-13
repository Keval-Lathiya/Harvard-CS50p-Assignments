Answer = input("the answer to the Great Question of Life, the Universe and Everything is : ")

if Answer.lower().strip() in (str(42),"forty-two","forty two"):
    print("Yes")
else:
    print("No")
