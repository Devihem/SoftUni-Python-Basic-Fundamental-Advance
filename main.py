def push_number(number):
    stack.append(number)


def delete_num():
    stack.pop()


num_queries = int(input())
stack = []
for i in range(num_queries):
    query = input()
    query_type,*idk = query.split()
    if query_type == "1":
        number = int(idk[0])
        push_number(number)
    elif query_type == "2":
        if stack:
            popped = stack.pop()

    elif query_type == "3":
        print(max(stack))
    else:
        print(min(stack))

stack_str = ', '.join(map(str, stack[::-1]))
print(stack_str)