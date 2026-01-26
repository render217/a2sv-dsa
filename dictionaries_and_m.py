# problem https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# submission https://www.hackerrank.com/challenges/30-dictionaries-and-maps/submissions/code/460947193


import sys
phone_book = {}
n = int(input())

for _ in range(n):
    entry = input().split(' ')
    phone_book[entry[0]] = entry[1]

for line in sys.stdin:
    key = line.strip()
    val = phone_book.get(key,None)
    if val:
        print(f'{key}={val}')
    else:
        print("Not found")
