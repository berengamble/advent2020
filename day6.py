from DataReader import DataReader


class AnswerParser:
    def __init__(self):
        self.records = []
        self._load_data()
        self._flattened_lists()

    def _load_data(self):
        self.raw = DataReader(day=6).as_raw()

    def _flattened_lists(self):
        self.records = [x.replace(' ', '') for x in " ".join(self.raw.split(
            '\n')).replace('  ', '\n').splitlines()]


class Form:
    def __init__(self, form_records):
        self.form_records = form_records
        self.num_answers = 0

    def count_answers(self):
        self.num_answers = sum(len(set(i)) for i in self.form_records)
        return self.num_answers

    def count_common_answers(self):
        # for i in self.form_records:
        print(self.form_records)
        # print(i)
        #self.num_answers = sum(len(set(i)) for i in self.form_records)
        return self.num_answers


answers = AnswerParser().records
print(Form(answers).count_answers())
# #Part 1
# sum_of_answers = Form(answers).count_answers()
print(Form(answers).count_common_answers())
