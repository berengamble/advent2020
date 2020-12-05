from DataReader import DataReader

class SeatNumberParser:

    def __init__(self):
        self.seat_ids = []

    def _load_data(self):
        return DataReader(day=5).as_raw()

    def _generate_id(self, seat):        
        return int(seat.replace('L', '0').replace('F', '0').replace('B', '1').replace('R', '1'), 2)
            
    def get_id_list(self):
        for i in self._load_data().splitlines():
            self.seat_ids.append(self._generate_id(i))
        return self.seat_ids

class SeatIds:

    def __init__(self, seat_ids):
        self.seat_ids = seat_ids

    def get_highest(self):
        return max(self.seat_ids)

    def find_my_seat(self):
        self.seat_ids.sort()
        missing = set(
                range(
                    self.seat_ids[0],
                    self.seat_ids[-1]+1
                )) - set(self.seat_ids)
        return missing.pop()

data = SeatNumberParser().get_id_list()
#Part 1
print(SeatIds(data).get_highest())
#Part 2
print(SeatIds(data).find_my_seat())

