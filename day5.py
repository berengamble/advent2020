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
    
    def find_my_seat2(self):
        summed_values = sum(x for x in range(min(self.seat_ids), max(self.seat_ids)+1))
        missing_number = summed_values - sum(x for x in self.seat_ids)
        return missing_number
    
    def find_my_seat3(self):
        
        first_loop = True
        for k, v in enumerate(self.seat_ids):
            if first_loop:
                if v > self.seat_ids[k+1]:
                    higher = v
                    lower = self.seat_ids[k+1]
                else:
                    higher = self.seat_ids[k+1]
                    lower = v

                first_loop = False
                continue
            if v > lower and v < higher:
                lower = v
            if v < higher and :
                higher = v
        # print(higher)
        # print(lower)
        print(lower - higher)


data = SeatNumberParser().get_id_list()
#Part 1
#print(SeatIds(data).get_highest()) # 714 - correct answer
#Part 2
print(SeatIds(data).find_my_seat3())

