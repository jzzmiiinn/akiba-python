correct_pin = 1234
n = 0
while n<3:
    trial=int(input("Enter your pin: "))
    n+=1
    if(trial==correct_pin):
        print("Successful")
        break
    else:
        print("Attempt remaining:",3-n)