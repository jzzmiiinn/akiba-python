largest=0
smallest=0
sum=0
average=0
count_even=0
count_odd=0

for i in range(10):
    num=int(input("Enter the number: "))
    sum+=num
    if num%2==0:
        count_even+=1
    else:
        count_odd+=1
    if i == 0:
        largest = num
        smallest = num
    else:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

average=sum/10

print("The largest number is:", largest)
print("The smallest number is:", smallest)
print("The sum of the given ten numbers is:", sum)
print("The average of the given ten numbers is:", average)
print("The number of even numbers in the given ten numbers is:", count_even)
print("The number of odd numbers in the given ten numbers is:", count_odd)