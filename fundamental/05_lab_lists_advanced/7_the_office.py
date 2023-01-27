workers_happiness_list = [int(happiness) for happiness in input().split()]
happy_factor = int(input())
improved_happiness_list = list(map(lambda happiness_up: happiness_up * happy_factor, workers_happiness_list))
happy_workers = len(list(filter(lambda worker_over_avg_happiness:
                                sum(improved_happiness_list) / len(improved_happiness_list) < worker_over_avg_happiness,
                                improved_happiness_list)))
if happy_workers >= len(workers_happiness_list) / 2:
    print(f"Score: {happy_workers}/{len(workers_happiness_list)}. Employees are happy!")
else:
    print(f"Score: {happy_workers}/{len(workers_happiness_list)}. Employees are not happy!")
