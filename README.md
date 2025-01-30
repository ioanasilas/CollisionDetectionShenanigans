# Collision Detection Algorithms in 2D – Benchmarking Time Complexity

This repository contains a benchmarking program for measuring the execution times of various 2D collision detection algorithms, including:

- AABB (Axis-Aligned Bounding Box)
- SAT (Separating Axis Theorem)
- Circle-Circle
- Circle-Line
- Line-Line

## Types of Tests

The program includes four test categories that evaluate different collision scenarios:

### 1. Random Tests (random)
These tests randomly generate shapes of different sizes and positions on the canvas.

Available random tests:
- circleCircleRandom
- aabbRandom
- lineLineRandom
- polygonPolygonRandom
- circleLineRandom

### 2. No Overlap Tests (nooverlap)
Shapes are placed across the canvas to ensure zero intersections between them.

Available no-overlap tests:
- circleCircleNoOverlap
- aabbNoOverlap
- lineLineNoOverlap
- polygonPolygonNoOverlap
- circleLineNoOverlap

### 3. Full Overlap Tests (overlap)
All generated shapes are placed in the same position to force maximum intersection.

Available full-overlap tests:
- circleCircleOverlap
- aabbOverlap
- lineLineOverlap
- polygonPolygonOverlap
- circleLineOverlap

### 4. Grid Overlap Tests (gridoverlap)
Shapes are positioned across multiple grid cells. We wanted to ensure that every shape intersects with all other shapes in its assigned grid region.

Available grid-overlap tests:
- circleCircleGridOverlap
- aabbGridOverlap
- lineLineGridOverlap
- polygonPolygonGridOverlap
- circleLineGridOverlap

## Instructions for Running the Program

To run the benchmark, open `main.py` and modify the algo_name_test_type variable to select the desired test:

```python
# What would you like to test?
algo_name_test_type = "circleLineGridOverlap"
```

This variable is based on the predefined dictionaries that may be seen in the source codes. So, users can check which tests are available and select the one they want.

### Configuring Test Parameters

Additional settings, such as the number of runs and points used in testing, can be modified inside shared_data.py.

## Output and Saved Results

When you run the program, three folders are created automatically to store results:

1. **collision_test_avg_results** – Contains CSV files summarizing the average execution times for each algorithm and test type.
2. **collision_test_detailed_results** – Stores CSV files with execution times for each individual run.
3. **collision_visual_outputs** – Saves images of every run to visualize the benchmarked tests.

### Existing Results in the Repository

The repository already contains folders with benchmarking results that were used in our research paper. These folders include the CSV files for execution times and the corresponding visual outputs. They serve as a reference for transparency. We wanted others to be able to verify and analyze our benchmarking process. If you notice anything weird, please let us know. :)

If you would like to generate your own results, modify the test parameters in `main.py` and `shared_data.py`, and run the program to create fresh benchmarking data.

---

This README provides an overview of how to use the program and understand the saved results. If you have any questions, feel free to reach out to us!
