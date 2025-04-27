#Ask user to enter a number
number = int(input("Please enter any number: "))
sum = 0
temp = number

while temp > 0:
    factorial = 1
    i = 1
    reminder = temp%10

    while i <= reminder:
        factorial = factorial*i
        i = i + 1
    
    print("\n Factorial of %d = %d" %(reminder, factorial))
    sum = sum + factorial
    temp = temp//10

#display output

print("\n Sum of Factorials of a Given Number %d = %d" %(number, sum))

if sum == number:
    print(" %d is a Strong Number" %number)
else:
    print(" %d is not a Strong Number" %number)