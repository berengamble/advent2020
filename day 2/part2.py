class ReadData:
    def __init__(self):
        self.raw_data = None
        self._read_data()
        
    def _read_data(self):
        with open('input.txt') as f:
            self.raw_data = f.read().splitlines()

    def as_raw(self):
        return self.raw_data

class Convert:
    def __init__(self, raw_input):
        
        parts = raw_input.split()
        
        self.positionA = parts[0].split("-")[0]
        self.positionB = parts[0].split("-")[1]
        self.required_char = parts[1][:-1]
        self.value = parts[2]
    
    def to_dict(self):
        return {
            "positionA" : int(self.positionA),
            "positionB" : int(self.positionB),
            "required_char" : self.required_char,
            "value" : self.value,
        }

passwords = []

for i in ReadData().as_raw():
    passwords.append(
        Convert(i).to_dict()
    )

num_valid_passwords = 0

for i in passwords:
    positionA = bool(i['value'][i['positionA']-1] is i['required_char'])
    positionB = bool(i['value'][i['positionB']-1] is i['required_char'])
    
    if positionA ^ positionB:
        num_valid_passwords += 1    
    
print(num_valid_passwords)
    