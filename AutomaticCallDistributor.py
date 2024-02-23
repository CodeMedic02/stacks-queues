# Name: Trent Adams
# Date: 2024-01-21

from Queue import Queue
from Call import Call
from datetime import date
import time   # use to pause the application.
import random # use to generate random number.


print("Name: ", "Trent Adams")
print("Date: ", date.today())
print()


calls = []

# read call records into the list.
input_file_name = "CallsData.csv"
with open(input_file_name) as infile:
    for line in infile:
        split_line = line.split(",")
        client_id = int(split_line[0])
        client_name = split_line[1]
        client_phone = split_line[2]

        # Create a "Call" object based on the data from the line and
        # add the "Call" object to the calls list.
        calls.append(Call(client_id, client_name, client_phone))


# Queue object for our calls.
calls_waiting = Queue()
call_number = 0

seconds = int(input("How many seconds do you want to simulate? "))

# Run the simulation for the given number of seconds.
for i in range(seconds):
    print("-" * 40)
    time.sleep(2)   # Pause application for the given number of seconds.
    random_event = random.randint(1, 3)

    # Do an event based on random event number.
    if random_event == 1:
        print("Call received. Caller added to queue.")
        calls_waiting.enqueue(calls[call_number])
        call_number += 1    # Set up the next call.
        print("\tNumber of calls waiting in queue: ", calls_waiting.get_length())

    elif random_event == 2:
        print("Call sent to representative for service.")
        if calls_waiting.get_length() > 0:
            print("Caller information: ")
            print(calls_waiting.dequeue())
        else:
            print("The call waiting queue is empty.")
        print("\tNumber of calls waiting in queue: ", calls_waiting.get_length())
    else:
        print("Nothing happened during this second time.")
        print("\tNumber of calls waiting in queue: ", calls_waiting.get_length())

print("\nThe 'Automatic Call Distributor simulation' has completed.")


