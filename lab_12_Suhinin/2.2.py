
def queue_with_timeout(customers, service_time):
    done = 0
    wasted = 0
    current_time = 0
    for arrival,max_wait in customers:
        if current_time < arrival:
            current_time = arrival
        waiting_time = current_time - arrival
        if waiting_time > max_wait:
            wasted += 1
        else:
            done += 1
            current_time += service_time
    return f"(Обслужено: {done}  Втрачено: {wasted})"
print(queue_with_timeout([(0,10),(1,10),(2,10)],2))