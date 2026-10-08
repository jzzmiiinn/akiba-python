number=10
count=0
num=0

while num!=number:
    num=int(input("Guess the number:"))
    count+=1

print("Congratulations!")
print("You guessed the number in",count,"attempts.")