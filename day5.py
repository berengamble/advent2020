from DataReader import DataReader

class SeatNumberParser:

    def __init__(self):
        self.seat_ids = []
        self._seat_ids_list()

    def _load_data(self):
        return DataReader(day=5).as_raw()

    def _generate_id(self, seat):
        row    = int(seat[0:7].replace('F', '0').replace('B', '1'), 2)
        column = int(seat[7:10].replace('L', '0').replace('R', '1'), 2)
        return row * 8 + column
            
    def _seat_ids_list(self):
        for i in self._load_data().splitlines():
            self.seat_ids.append(self._generate_id(i))

    def get_highest_id(self):
        return max(self.seat_ids)

    def find_my_seat_id(self):
        self.seat_ids.sort()
        missing = set(
                range(
                    self.seat_ids[0],
                    self.seat_ids[-1]+1
                )) - set(self.seat_ids)
        return missing.pop()

#Part 1
print(SeatNumberParser().get_highest_id())
#Part 2
print(SeatNumberParser().find_my_seat_id())

