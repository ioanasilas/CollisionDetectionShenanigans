import csv
from shared_data import times

# to do: get a csv for every function type, for every size we will have
# we can use a size dictionary or something
# this is a prototype only

def save_exec_time(times, filename= "execution_times.csv"):
  with open(filename, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(["Run number", "Execution time (s)"])
    for i, time in enumerate(times):
      writer.writerow([i, time])