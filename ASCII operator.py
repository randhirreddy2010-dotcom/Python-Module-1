print(ord("A"))
print(ord("a"))
print(ord("0"))
print(ord("@"))

print(chr(65))
print(chr(97))

char = input("Enter a single character:")
if type(char) is str and len(char) == 1:
    print("This is a valid input")
else:
    print("PLease enter ONE character")

ascii_value = ord(char)
print(f"Character: {char}")
print(f"ASCII value: {ascii_value}")

if ascii_value >= 65 and ascii_value <= 90:
    print("Type: Uppercase Letter")
elif ascii_value >= 97 and ascii_value <= 122:
    print("Type: Lowercase Letter")
elif ascii_value >= 48 and ascii_value <= 57:
    print("Type: Digit")
elif ascii_value == 32:
    print("Type: Space")
else:
    print("Type: Special Character")

print("ASCII value checker")
print("=" * 40)
if type(char) is str and len(char) == 1:
    ascii_value = ord(char)
    print(f"\nCharacter: '{char}'")
    print(f"ASCII value: {ascii_value}")

    print("\nCharacter Type: ", end="")

    if ascii_value >= 65 and ascii_value <= 90:
        print(" Type: Uppercase Letter")
    elif ascii_value >= 97 and ascii_value <= 122:
        print(" Type: Lowercase Letter")
    elif ascii_value >= 48 and ascii_value <= 57:
        print(" Type: Digit")
    elif ascii_value == 32:
        print(" Type: Space") 
    else:
        print(" Type: Special Character")
else:
    print("\nError: Please enter exactly ONE character!")