from DataReader import DataReader

data = list(map(int, DataReader(day=1).as_raw().splitlines()))

for num in data:
    remainder = 2020 - num
    if [ i for i in data if i == remainder ]:
        print( num * remainder )
        break