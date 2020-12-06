a=[]
n=int(input('Enter the size of array'))
for i in range(n):
    b=int(input())
    a.append(b)
while n!=0:
    print(a.pop())
    n=n-1
