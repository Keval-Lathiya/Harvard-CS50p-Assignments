

test_str = input("Write anything : ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
new_str = ''.join(character for character in test_str if character not in vowels)

print (new_str)
