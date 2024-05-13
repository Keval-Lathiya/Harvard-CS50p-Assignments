def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha():
        return False
    try:
        if [x.isdigit() for x in s].index(True):
            first_digit_index = [x.isdigit() for x in s].index(True)
            if first_digit_index < 2 or s[first_digit_index] == '0' :
                return False
    except:
        return True
    if not s[first_digit_index:].isdigit():
        return False
    if any(c in s for c in ". ,;:!-_?\"'()"):
        return False
    if s[:].isalpha():
        return False
    return True




main()


