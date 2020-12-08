from parse import parse
from DataReader import DataReader
import time


class Instructions:

    def __init__(self):
        self.machine_code = []
        self._load_instructions()

    def _load_instructions(self):
        self.lines = DataReader(day=8).as_raw().splitlines()
        for i in self.lines:
            self.machine_code.append(parse("{} {}", i))
        # add END instruction
        self.machine_code.append(('end', '0'))


class Processor:
    def __init__(self, machine_code):
        self.machine_code = machine_code
        self.pointer = 0
        self.acc = 0
        self.part1()

    def part1(self):

        NOP = 'nop'
        ACC = 'acc'
        JMP = 'jmp'
        END = 'end'

        executed = []
        while True:
            code, value = self.machine_code[self.pointer][0], self.machine_code[self.pointer][1]

            if self.pointer not in executed:
                executed.append(self.pointer)
            else:
                break

            if code == NOP:  # good
                self.pointer += 1
                continue
            if code == ACC:
                self.acc += int(value)
                self.pointer += 1
            if code == JMP:
                self.pointer += int(value)
            # print("{} {:>3} acc={:<4} pointer={}".format(
            #    code, value, self.acc, self.pointer))
            if code == END:
                break


machine_code = Instructions().machine_code
print(Processor(machine_code).acc)
