n,t = map(int,input().split())
a = list(map(int,input().split()))


curr_time = 0
max_read = 0
left = 0

for right in range(n):
    curr_time += a[right]

    while curr_time > t: 
        curr_time -= a[left]
        left+=1
    
    max_read = max(max_read,right - left + 1)

print(max_read)
