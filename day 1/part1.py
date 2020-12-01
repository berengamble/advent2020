with open('input.txt') as f:
    arr = list(map(int, f.read().splitlines()))

for num in arr:
    remainder = 2020 - num
    if [ i for i in arr if i == remainder ]:
        print( num * remainder )
        break