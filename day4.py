from DataReader import DataReader

class PassportRecord:
    def __init__(self, record):
        self.record = record

class PassportDataParser:
    def __init__(self):
        self.records = []
        self._to_dicts()

    def _load_data(self):
        return DataReader(day=4).as_raw()

    def _flattened_list(self):
        return  " ".join(self._load_data().split('\n')).replace('  ', '\n').splitlines()

    def _to_dicts(self):
        for i in self._flattened_list():
            d = dict(x.split(":") for x in i.split(" "))
            self.records.append(d)

class PassportValidator:
    def __init__(self):
        self.valid_passports = 0
        self.required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        self.passport_data = PassportDataParser().records
        self.validation_rules
    
    def validate(self):
        for i in self.passport_data:
            filled = set(k for k in i.keys())
            if self.required.issubset(filled):
                self.valid_passports += 1

        return self.valid_passports
        
            
results = PassportValidator().validate()
print(results)
