def fcfs(jobs, arrival_time, burst_time):
    final_time = 0
    gantt_chart = [0]
    for i in range(len(jobs)):
        print(jobs[i], arrival_time[i], burst_time[i])



j = list("ABC")
a = list("012")
b = list("234")

fcfs(j, a, b)