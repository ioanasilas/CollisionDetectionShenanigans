# Title - blah blah blah

Print("Hello, World!")

## Tests
The program currently contains 4 types of tests, and they are:
### random
This `test_type` randomly generates the sizes and positions of the shapes
- `circleCircleRandom`
- `aabbRandom`
- `lineLineRandom`
- `polygonPolygonRandom`
- `circleLineRandom`

### nooverlap
This `test_type` spreads the generated shapes across the canvas to make sure there are 0 intersections
- `circleCircleNoOverlap`
- `aabbNoOverlap`
- `lineLineNoOverlap`
- `polygonPolygonNoOverlap`
- `circleLineNoOverlap`

### overlap
This `test_type` places all the generated shapes in one position to make sure all of them intersect with eachother
- `circleCircleOverlap`
- `aabbOverlap`
- `lineLineOverlap`
- `polygonPolygonOverlap`
- `circleLineOverlap`

### gridoverlap
This `test_type` places all the generated shapes across multiple positions `n` making a grid. Every shape has to intersect with all the other shapes in their assigned grid
- `circleCircleGridOverlap`
- `aabbGridOverlap`
- `lineLineGridOverlap`
- `polygonPolygonGridOverlap`
- `circleLineGridOverlap`


## Instructions
Inside of `main.py`, change the `algo_name_test_type` value to one of the tests mentioned above and run the program.
Values such as `runs`, and `PointsTesting` can be changed inside of the `shared_data.py` file.

After running the program, 3 types of data will be saved in folders:
- Average Results - Saves CSV files of the average results for a test type
- Detailed Results - Saves CSV files of more detailed results for every run done
- Visual Outputs - Saves Pictures of every run done

