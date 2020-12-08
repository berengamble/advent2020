from parse import parse
import re
from DataReader import DataReader

import pprint


class BaggageRuleParser:
    def __init__(self):
        self.records = []
        self._load_data()

    def _load_data(self):
        self.raw = DataReader(day=7).as_raw()

    def rules(self):
        for i in self.raw.split('.\n'):
            data_row = parse("{} bags contain {}", i)
            matches = re.findall(r'(\d) ([\w\s]*) bag', data_row[1])
            bag = {
                data_row[0]: {
                    'must_contain': matches if matches else [(0)]
                }
            }
            self.records.append(bag)
        return self.records


# class BaggageChecker:
#     def __init__(self, rules):
#         self.rules = rules
#         self.num_with_shiny_gold = 0

#     def part1():


rules = BaggageRuleParser().rules()
print(rules)
