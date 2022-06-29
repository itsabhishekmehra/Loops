i=0
sum=0
while i<4:
    a=int(input('Enter the weight: '))
    sum=a+sum
    i+=1
print(sum)
if sum%5==0:
    print('All OKay')
else:
    print('Problem')