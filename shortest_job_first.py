def sjt_non(jobs, arrival_time, burst_time):
    final_time = 0
    gantt_chart = [0]
    for i in range(len(jobs)):
        if final_time < int(arrival_time[i]): # Adds idle time
            final_time += int(arrival_time[i])
            gantt_chart.append(final_time)

        else: 
            int_burst_time = [int(i) for i in burst_time] # finds shortest job first
            shortest_job = int_burst_time.index(min(int_burst_time))

            if final_time > int_burst_time[shortest_job]:
                gantt_chart.append(jobs[shortest_job])
                final_time = final_time + int_burst_time[shortest_job]
                gantt_chart.append(final_time)

            else: 
                gantt_chart.append(jobs[i])
                final_time = final_time + int(burst_time[i])
                gantt_chart.append(final_time)


    print(gantt_chart)

user_jobs = list(input("Please input Jobs: "))
job_AT = list(input("Please input arrival time: "))
job_BT = list(input("Pleae input burst time: "))

if len(user_jobs) != len(job_AT) or len(user_jobs) != len(job_BT):
    print("invalid input")

else: 
    sjt_non(user_jobs, job_AT, job_BT)

