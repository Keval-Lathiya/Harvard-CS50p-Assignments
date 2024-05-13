def change_case(str):
    res=""
    for i in str:
        if(i.isupper()):
            res+="_"+i.lower()
        else:
            res+=i
    return res

str = input("Enter the variable in camel case : ")
print(change_case(str))


