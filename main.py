import pygame
import pygame.gfxdraw
import sys
import math
import random
import time
from random_testing import circleCircleRandom, polygonPolygonRandom, circleLineRandom, aabbRandom, lineLineRandom, test_functions_random
from no_overlap_testing import circleLineNoOverlap, polygonPolygonNoOverlap, lineLineNoOverlap, circleCircleNonOverlap, aabbNoOverlap, test_functions_no_overlap
from full_overlap_testing import circleCircleFullOverlap, circleLineFullOverlap, polygonPolygonFullOverlap, lineLineFullOverlap, aabbFullOverlap, test_functions_overlap, test_functions_grid_overlap
from shared_data import shapes, times, pointsTestingDict, overlap_positions_testing
from csv_saves import *
import os

WHITE = (255, 255, 255)
RED = (200, 100, 100)
GREEN = (100, 200, 150)
GREY = (25, 25, 25)


pygame.init()
screen = pygame.display.set_mode((1024, 618))
pygame.display.set_caption("Collision Detection Tests")

# circleCircleRandom()
# aabbRandom()
# lineLineRandom()
# circleLineRandom()
# polygonPolygonRandom()


# make directory to save visual outputs and csv
base_dir = "collision_visual_outputs"
os.makedirs(base_dir, exist_ok=True)

random_dir = os.path.join(base_dir, "random")
no_overlap_dir = os.path.join(base_dir, "nooverlap")
overlap_dir = os.path.join(base_dir, "overlap")
grid_overlap_dir = os.path.join(base_dir, "gridoverlap")
os.makedirs(random_dir, exist_ok=True)
os.makedirs(no_overlap_dir, exist_ok=True)
os.makedirs(overlap_dir, exist_ok=True)
os.makedirs(grid_overlap_dir, exist_ok=True)

csv_dir = "collision_test_detailed_results"
os.makedirs(csv_dir, exist_ok=True)
random_dir_csv = os.path.join(csv_dir, "random")
no_overlap_dir_csv = os.path.join(csv_dir, "nooverlap")
overlap_dir_csv = os.path.join(csv_dir, "overlap")
grid_overlap_dir_csv = os.path.join(csv_dir, "gridoverlap")
os.makedirs(random_dir_csv, exist_ok=True)
os.makedirs(no_overlap_dir_csv, exist_ok=True)
os.makedirs(overlap_dir_csv, exist_ok=True)
os.makedirs(grid_overlap_dir_csv, exist_ok=True)

csv_dir_avg = "collision_test_avg_results"
os.makedirs(csv_dir_avg, exist_ok=True)

# what are we testing?
test_type = "overlap"
algo_name_test_type = "polygonPolygonOverlap"

# Only for overlap
# I didnt make the csv functionality for overlaps yet, but basically this
# is how many positions the shapes are gonna be split between. Default is 1

for k, v in pointsTestingDict.items():

    avgTime = 0.0
    # enough?
    total_runs = 0
    # get value for max Runs
    max_runs = pointsTestingDict[k]
    no_of_positions = overlap_positions_testing[k]
    # get key for points testing
    pointsTesting = k
    outline = 1
    running = True

    while running and total_runs < max_runs:
        screen.fill(GREY)
        shapes.clear()
        # polygonPolygonRandom()
        # circleLineRandom()
        # lineLineRandom()
        # aabbRandom()
        # circleCircleRandom()
        # circleLineNoOverlap()
        # aabbNoOverlap()

        if test_type == "random":
            if algo_name_test_type in test_functions_random:
                test_functions_random[algo_name_test_type](pointsTesting)
            else:
                print("We do not have a test like this.")
        elif test_type == "nooverlap":
            if algo_name_test_type in test_functions_no_overlap:
                test_functions_no_overlap[algo_name_test_type](pointsTesting)
            else:
                print("We do not have a test like this.")
        elif test_type == "overlap":
            if algo_name_test_type in test_functions_overlap:
                test_functions_overlap[algo_name_test_type](pointsTesting)
            else:
                print("We do not have a test like this.")
        elif test_type == "gridoverlap":
            if algo_name_test_type in test_functions_grid_overlap:
                test_functions_grid_overlap[algo_name_test_type](pointsTesting, no_of_positions)
            else:
                print("We do not have a test like this.")
        else:
            print("This test type does not exist.")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and (48 <= event.key <= 57):
                outline = int(chr(event.key))
        
        # timing just actual sorting, you're cool ioana \o/
        random.shuffle(shapes)
        print("Run: ", total_runs + 1)
        startTime = time.time()
        for i in range(len(shapes)):
            if shapes[i].intersecting == False:
                for v in range(len(shapes)):
                    if i == v:
                        continue
                    
                    if (shapes[i].intersects(shapes[v])):
                        shapes[i].intersecting = True
                        shapes[v].intersecting = True
                        intersects = True
                        break
            
            if shapes[i].intersecting == True:
                shapes[i].draw(screen, RED, outline)
            else:
                shapes[i].draw(screen, GREEN, outline)

        timeTaken = (time.time() - startTime)
        times.append(timeTaken)
        avgTime = avgTime + (timeTaken - avgTime) / (total_runs + 1)
        print("Time Taken: ", timeTaken)
        print("Current Average: ", avgTime)

        # all cases, add last
        if test_type == "random":
            save_path = os.path.join(random_dir, f"collision_output_{algo_name_test_type}_{pointsTesting}_run{total_runs + 1}.png")
            filename = os.path.join(random_dir_csv,f"execution_times_{algo_name_test_type}_{pointsTesting}.csv")
        elif test_type == "overlap":
            save_path = os.path.join(overlap_dir, f"collision_output_{algo_name_test_type}_{pointsTesting}_run{total_runs + 1}.png")
            filename = os.path.join(overlap_dir_csv,f"execution_times_{algo_name_test_type}_{pointsTesting}.csv")
        elif test_type == "gridoverlap":
            save_path = os.path.join(grid_overlap_dir, f"collision_output_{algo_name_test_type}_{pointsTesting}_run{total_runs + 1}.png")
            filename = os.path.join(grid_overlap_dir_csv,f"execution_times_{algo_name_test_type}_{pointsTesting}.csv")
        elif test_type == "nooverlap":
            save_path = os.path.join(no_overlap_dir, f"collision_output_{algo_name_test_type}_{pointsTesting}_run{total_runs + 1}.png")
            filename = os.path.join(no_overlap_dir_csv,f"execution_times_{algo_name_test_type}_{pointsTesting}.csv")
                
        pygame.display.flip()
        pygame.image.save(screen, save_path)
        print(f"Pygame visual saved as {save_path}")
        pygame.time.Clock().tick(60)

        total_runs += 1
    # after each batch of runs, append the average to this list
    averages[pointsTesting] = avgTime
    save_exec_time_detailed(pointsTesting, algo_name_test_type, times, filename)
    print(f"Execution times saved to \"execution_times_{algo_name_test_type}.csv\"")
    # go from 0 again after each batch
    times = []



pygame.quit()
avg_save_path = os.path.join(csv_dir_avg, f"collision_output_{algo_name_test_type}_averages.png")
filename_avg = os.path.join(csv_dir_avg, f"averages_for{algo_name_test_type}.csv")
# we then make a csv with averages for each algo; eg for aabb we will have averages for 10, 50, 100, 500, 1000, 10000 points in the same file
if test_type == "gridoverlap":
    save_exec_time_avg_grid_overlap(algo_name_test_type, averages, filename_avg)
else:
    save_exec_time_avg(algo_name_test_type, averages, filename_avg)

sys.exit()