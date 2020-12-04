class DataReader:
    def __init__(self, day):
        self.raw_data = None
        self.day = day
        self._read_data()
        
    def _read_data(self):
        with open('input/day' + str(self.day) + '.txt') as f:
            self.raw_data = f.read()

    def as_raw(self):
        return self.raw_data.rstrip()