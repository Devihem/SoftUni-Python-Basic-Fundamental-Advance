class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.result = 0
        self.counter_loop = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter_loop >= self.count:
            raise StopIteration
        return_result = self.result
        self.result += self.step
        self.counter_loop += 1
        return return_result


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
