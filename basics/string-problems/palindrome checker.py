text = input("Enter a text: ")
text = text.replace(" ", "")

if text == text[::-1]:
    print("This number/text is a palindrome.")
else:
    print("This number/text is not a palindrome.")
