class take_skip:
    def __init__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass




iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
