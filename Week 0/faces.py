

def convert(text):
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text

def main():
    user_input = input("Please enter a string: ")
    result = convert(user_input)
    print(result)


main()

