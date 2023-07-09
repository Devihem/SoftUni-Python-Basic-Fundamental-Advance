def fibonacci():
    nums = [0, 1, 1]
    yield nums[0]
    yield nums[1]
    yield nums[2]
    while True:
        num = nums[1] + nums[2]
        yield num
        nums[1], nums[2] = nums[2], num


generator = fibonacci()
for i in range(5):
    print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))
