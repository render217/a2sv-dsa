n, k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

val = -1
if k == 0:
    if a[0] > 1:
        val = 1
elif k == n:
    val = a[-1]
elif 0 < k < n:
    if a[k-1] != a[k]:
        val = a[k-1]
print(val)