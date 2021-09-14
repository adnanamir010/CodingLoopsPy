a=0
b=1
upperLimit=int(input("Please enter how many numbers you want from the series: "))
output=[0]
for i in range(1,upperLimit):
    c=a+b
    a=b
    b=c
    output.append(a)
print (*output)