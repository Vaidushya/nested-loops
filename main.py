#taking input in words 
text = input("Please enter your own word : ")
ch = input("Please enter your own Character : ")

i = 0 
count = 0

while(i < len(text)):

    if text[i] == ch:
        count = count + 1

    i = i+1

#Final result
print("The total Number of Times ", ch, " has Occurred = " , count)