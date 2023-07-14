def solution():
    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        m = 0
        while m < n:
            yield next(seq)
            m += 1

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(list(take(5, halves())))