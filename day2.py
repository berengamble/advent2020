from DataReader import DataReader

class PasswordParser:
    def __init__(self, raw_input):
        
        parts = raw_input.split()
        
        self.min = parts[0].split("-")[0]
        self.max = parts[0].split("-")[1]
        self.required_char = parts[1][:-1]
        self.value = parts[2]
    
    def to_dict(self):
        return {
            "min" : int(self.min),
            "max" : int(self.max),
            "required_char" : self.required_char,
            "value" : self.value,
        }

passwords = []

data = DataReader(day=2).as_raw()

for i in data:
    passwords.append(
        PasswordParser(i).to_dict()
    )

num_valid_passwords = 0

for i in passwords:
    
    if i['value'].count(i['required_char']) in range(i['min'], i['max']+1):
        num_valid_passwords += 1
    
print(num_valid_passwords)
    
class ReadData:
    def __init__(self):
        self.raw_data = None
        self._read_data()
        
    def _read_data(self):
        with open('input.txt') as f:
            self.raw_data = f.read().splitlines()

    def as_raw(self):
        return self.raw_data

class PasswordParser:
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
        PasswordParser(i).to_dict()
    )

num_valid_passwords = 0

for i in passwords:
    positionA = bool(i['value'][i['positionA']-1] is i['required_char'])
    positionB = bool(i['value'][i['positionB']-1] is i['required_char'])
    
    if positionA ^ positionB:
        num_valid_passwords += 1    
    
print(num_valid_passwords)
    