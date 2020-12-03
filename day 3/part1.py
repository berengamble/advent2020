class ReadData:
    def __init__(self):
        self.raw_data = None
        self._read_data()
        
    def _read_data(self):
        with open('input.txt') as f:
            self.raw_data = f.read()

    def as_raw(self):
        return self.raw_data

class Convert:
    def __init__(self, raw_input):
        self.raw_input = raw_input
    
    def to_list_of_lists(self):
        return self.raw_input.splitlines()

class Forest:
    def __init__(self, pattern):
        self.pattern = pattern

raw_data = ReadData().as_raw()
forest = Convert(raw_data).to_list_of_lists()
forest_width = len(forest[0])

X_MOVEMENTS = 3
Y_MOVEMENTS = 1
TREE = '#'


visited_coordinates = []
x, y = 0, 0

for i in forest:
    
    visited_coordinates.append([x,y])
    x += X_MOVEMENTS
    y += Y_MOVEMENTS

trees_seen = 0

for i in visited_coordinates:

    x = i[0] % forest_width
    y = i[1]

    if forest[y][x] == TREE:
        trees_seen += 1

print(trees_seen)