import csv
from shared_data import times, averages

# to do: get a csv for every function type, for every size we will have
# we can use a size dictionary or something
# this is a prototype only

def save_exec_time_detailed(pointsTesting, algo_name_test_type, times, filename):
  with open(filename, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow([f"Testing for {pointsTesting} points", algo_name_test_type])
    writer.writerow(["Run number", "Execution time (s)"])
    for i, time in enumerate(times):
      writer.writerow([i + 1, time])

def save_exec_time_avg(pointsTesting, algo_name_test_type, averages, filename):
  with open(filename, mode = 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([f"Testing {algo_name_test_type}"])
    writer.writerow(["No. points", "Avg. execution time (s)"])
    for avg_time in averages:
      writer.writerow([{pointsTesting}, avg_time])