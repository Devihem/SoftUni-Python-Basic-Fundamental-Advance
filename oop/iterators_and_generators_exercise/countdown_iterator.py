class countdown_iterator:
    def __init__(self, period):
        self.period = period
        self.current_point = period + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_point == 0:
            raise StopIteration
        self.current_point -= 1
        return self.current_point


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
