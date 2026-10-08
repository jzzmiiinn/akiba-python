n = int(input("Enter a number:"))
even_count = 0
odd_count = 0
sum = 0

for i in range(1,n+1):
    sum+=i
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1

print("The sum of all the numbers is:",sum)
print("The number of even numbers is:",even_count)
print("The number of odd numbers is:",odd_count)