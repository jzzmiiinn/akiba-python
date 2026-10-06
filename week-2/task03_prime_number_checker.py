num = int(input("Enter a number: "))

if num==0 or num==1:
    print(num, "-> Not prime")
elif num == 2:
    print(num, "-> Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "-> Not prime")
            break
    else:
        print(num, "-> Prime")