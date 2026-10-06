word=input("Enter the word:")

word=word.lower()

reversed=word[::-1]

if word==reversed:
    print("It is a palindrome")
else:
    print("It is not a palindrome")