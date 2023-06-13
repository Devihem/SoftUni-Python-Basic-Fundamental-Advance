job_cycles = [int(x) for x in input().split(', ')]
specific_job_index = int(input())
job_to_be_done = job_cycles[specific_job_index]

total_cpu_type = 0

for index in range(len(job_cycles)):
    if job_to_be_done > job_cycles[index]:
        total_cpu_type += job_cycles[index]
    elif job_to_be_done == job_cycles[index]:
        if index <= specific_job_index:
            total_cpu_type += job_cycles[index]

print(total_cpu_type)
