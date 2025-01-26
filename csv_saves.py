import csv
from shared_data import times, averages, overlap_positions_testing

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

def save_exec_time_avg(algo_name_test_type, averages, filename):
  with open(filename, mode = 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([f"Testing {algo_name_test_type}"])
    writer.writerow(["No. points", "Avg. execution time (s)"])
    for key, avg_time in averages.items():
      writer.writerow([{key}, avg_time])
      
def save_exec_time_avg_grid_overlap(algo_name_test_type, averages, filename):
  with open(filename, mode = 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([f"Testing {algo_name_test_type}"])
    writer.writerow(["No. points", "No. positions" , "Avg. execution time (s)"])
    for key, avg_time in averages.items():
      writer.writerow([{key}, overlap_positions_testing[key], avg_time])