# -- homework -- 
num = int(input("Enter a decimal number: "))

binary = ""

while num > 0:
    r = num % 2
    binary = str(r) + binary
    num //= 2

print(f"Binary of the given number is {binary}")