def tribonacci_sequence_4_4(times_to_loop):
    sequences_list = []
    container_1 = 1
    container_2 = 0
    container_3 = 0
    result = 1
    for number in range(1, times_to_loop + 1):
        sequences_list.append(result)
        result = container_3 + container_2 + container_1
        container_3 = container_2
        container_2 = container_1
        container_1 = result
    return sequences_list


sequences = int(input())
print(*tribonacci_sequence_4_4(sequences))

