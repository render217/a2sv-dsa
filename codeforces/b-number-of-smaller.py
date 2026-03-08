n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
 
 
ans = []
 
j = 0
for i in range(m):
    while j < n and a[j] < b[i]:
        j+=1
    ans.append(j)
 
 
print(" ".join(map(str,ans)))
