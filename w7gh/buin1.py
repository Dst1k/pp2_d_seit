def filt(x):
    if x % 2 == 1:
        return True
    else:
        return False
n = int(input())
num = list(map(int,input().split()))
odd = filter(filt,num)
for i in odd:
    print(i,end=" ")