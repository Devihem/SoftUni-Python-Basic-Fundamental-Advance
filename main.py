bana = {1, 2, 3, 4, 5, 6}
nana = {7, 8}

function = {
    'ADD': lambda x,y: [x.union(y)],
}

z = function["ADD"](bana,nana)
print(z)