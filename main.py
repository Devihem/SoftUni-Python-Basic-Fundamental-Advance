def test(*dasda):
    print(type(dasda))

z, *x = input().split()

test(*x)
