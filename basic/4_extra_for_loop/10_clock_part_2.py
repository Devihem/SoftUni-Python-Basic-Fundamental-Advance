for i in range(0, 24 * 60 * 60):
    hours = i // (60 * 60)
    minuets = (i // 60) % 60
    seconds = i % 60
    print(f"{hours} : {minuets} : {seconds}")