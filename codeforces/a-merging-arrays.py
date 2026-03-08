n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

l = 0
r = 0

res = []

while l < n and r < m:
    if a[l] < b[r]:
         res.append(a[l])
         l+=1
    else:
        res.append(b[r])
        r+=1

while l < n:
     res.append(a[l])
     l+=1
while r < m:
     res.append(b[r])
     r+=1

print(" ".join(list(map(str,res))))
