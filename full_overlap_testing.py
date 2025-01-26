import random
import math
from shapes import Point, Polygon, Circle, Line, Rectangle
from shared_data import shapes, pointsTestingDict

# circleCircleRandom()
# aabbRandom()
# lineLineRandom()
# circleLineRandom()
# polygonPolygonRandom()


xPixels = 1024
yPixels = 618
density = 1

# Random points generation

def circleCircleFullOverlap(pointsTesting, n = 1):
    shapesTesting = pointsTesting
        
    cols = math.ceil(math.sqrt(n))
    rows = math.ceil(n/cols)
    
    gridX = round(xPixels/cols)
    gridY = round(yPixels/rows)
    
    grid = []
    
    for i in range(0, cols):
        for j in range(0, rows):
            newPoint = Point(gridX/2 + (i * gridX), gridY/2 + (j * gridY))
            grid.append(newPoint)
            
    maxRadius = int(min(gridX, gridY)/2)

    for i in range(0, shapesTesting):
        index = i % n
        randomRadius = random.randint(1, maxRadius)
        randomPoint = Point(grid[index].x, grid[index].y)

        newCircle = Circle(randomPoint, randomRadius)
        shapes.append(newCircle)

def aabbFullOverlap(pointsTesting, n = 1):
    cols = math.ceil(math.sqrt(n))
    rows = math.ceil(n/cols)
    
    gridX = round(xPixels/cols)
    gridY = round(yPixels/rows)
    hX = round((xPixels/cols)/2)
    hY = round((yPixels/rows)/2)
    
    grid = []
    
    for i in range(0, cols):
        for j in range(0, rows):
            newPoint = Point(gridX/2 + (i * gridX), gridY/2 + (j * gridY))
            grid.append(newPoint)
    
    shapesTesting = int(pointsTesting/2)

    for i in range(shapesTesting):
        index = i % n
        randomP1 = Point(random.randint(int(grid[index].x) - hX, int(grid[index].x)), random.randint(int(grid[index].y) - hY, int(grid[index].y)))
        randomP2 = Point(random.randint(int(grid[index].x), int(grid[index].x) + hX), random.randint(int(grid[index].y), int(grid[index].y) + hY))

        newBox = Rectangle(randomP1, randomP2)
        shapes.append(newBox)

def lineLineFullOverlap(pointsTesting, n = 1):
    cols = math.ceil(math.sqrt(n))
    rows = math.ceil(n/cols)
    
    gridX = round(xPixels/cols)
    gridY = round(yPixels/rows)
    hX = round((xPixels/cols)/2)
    hY = round((yPixels/rows)/2)
    
    grid = []
    for i in range(0, cols):
        for j in range(0, rows):
            newPoint = Point(gridX/2 + (i * gridX), gridY/2 + (j * gridY))
            grid.append(newPoint)
    
    shapesTesting = int(pointsTesting / 2)

    for i in range(shapesTesting):
        index = i % n
        randomP1 = Point(random.randint(int(grid[index].x) - hX, int(grid[index].x) + hX), random.randint(int(grid[index].y) - hY, int(grid[index].y) + hY))
        while True:
          if abs(grid[index].x - randomP1.x) < 2  and abs(grid[index].y - randomP1.y) < 2:
            randomP1.x = random.randint(int(grid[index].x) - hX, int(grid[index].x) + hX)
            randomP1.y = random.randint(int(grid[index].y) - hY, int(grid[index].y) + hY)
          else:
            break
        center = grid[index]
        
        dx = center.x - randomP1.x 
        dy = center.y - randomP1.y
        magnitude = math.sqrt(dx**2 + dy**2)
        
        newPoint = Point(dx/magnitude, dy/magnitude)        
        randomP2 = Point(round(randomP1.x + (newPoint.x * (magnitude * 2))), round(randomP1.y + (newPoint.y * (magnitude* 2))))

        newLine = Line(randomP1, randomP2)
        shapes.append(newLine)

def polygonPolygonFullOverlap(pointsTesting, n = 1):
    cols = math.ceil(math.sqrt(n))
    rows = math.ceil(n/cols)
    
    gridX = round(xPixels/cols)
    gridY = round(yPixels/rows)
    hS = round(min(gridX, gridY)/2)
    
    grid = []
    for i in range(0, cols):
        for j in range(0, rows):
            newPoint = Point(gridX/2 + (i * gridX), gridY/2 + (j * gridY))
            grid.append(newPoint)
            
    points_used = 0
    shapesTesting = 0
    maxEdges = 10

    edgeNumArr = []
    
    while points_used < pointsTesting:
        #print(points_used)
        if points_used >= pointsTesting - (maxEdges + 3):
            if points_used < pointsTesting - 5:
                num_edges = random.randint(3, pointsTesting - (points_used + 3))
                edgeNumArr.append(num_edges)
                points_used += num_edges
            
            edgeNumArr.append(pointsTesting - points_used)
            points_used += pointsTesting - points_used
            shapesTesting += 1
        else:
            num_edges = random.randint(3, 10)
            edgeNumArr.append(num_edges)
            points_used += num_edges

        shapesTesting += 1

    # print(shapesTesting, points_used)
    # each poly has between 3 and 10 edges
    # get how many polys we will get
    # leftover_points = pointsTesting % num_edges

    polygons = []

    i = 0
    for edgesInPolygon in edgeNumArr:
        # we can use Valtr algorithm
        index = i % n
        randomPosX = int(grid[index].x)
        randomPosY = int(grid[index].y)
        X = random.sample(range(randomPosX - hS, randomPosX+hS), edgesInPolygon) 
        Y = random.sample(range(randomPosY - hS, randomPosY+hS), edgesInPolygon) 

        # sort X, Y to get min, max
        X.sort()
        Y.sort()

        minX, maxX = X[0], X[-1]
        minY, maxY = Y[0], Y[-1]

        # get rid of min and max
        X1 = X[1:-1]
        Y1 = Y[1:-1]

        # divide remaining into 2 groups
        xVec = []
        yVec = []

        lastTop = minX
        lastBot = minX

        for x in X1:  # Loop through X1 to calculate differences
            if bool(random.getrandbits(1)):
                xVec.append(x - lastTop)  # add dif to xVec
                lastTop = x  # update lastTop to current x coord
            else:
                xVec.append(lastBot - x)
                lastBot = x

        # Close the shape by adding final points
        xVec.append(maxX - lastTop)
        xVec.append(lastBot - maxX)

        lastTop = minY
        lastBot = minY

        for y in Y1:  # Loop through Y1 to calculate differences
            if bool(random.getrandbits(1)):
                yVec.append(y - lastTop)  # add dif to yVec
                lastTop = y  # update lastTop to current y coord
            else:
                yVec.append(lastBot - y)
                lastBot = y

        # Close the shape by adding final points
        yVec.append(maxY - lastTop)
        yVec.append(lastBot - maxY)

        # Shuffle points together
        points = list(zip(xVec, yVec))
        random.shuffle(points)

        # Create vectors with shuffled coordinates
        vectors = [Point(x, y) for x, y in points]

        # Sort vectors by angle
        vectors.sort(key=lambda v: math.atan2(v.y, v.x))

        # Lay the points end to end
        x, y = 0, 0
        minPolX, minPolY = 0, 0
        polygon_points = []

        for v in vectors:
            polygon_points.append(Point(x, y))
            x += v.getX()
            y += v.getY()

            minPolX = min(minPolX, x)
            minPolY = min(minPolY, y)

        # move polygon to original min/max coordinates
        xShift = minX - minPolX
        yShift = minY - minPolY
        translated_polygon = Polygon([Point(p.x + xShift, p.y + yShift) for p in polygon_points])

        polygons.append(translated_polygon)
        i += 1

    # print(polygons)
    # print(num_edges)
    # print(no_of_polys)

    # Add every polygon to shapes
    shapes.extend(polygons)


def circleLineFullOverlap(pointsTesting, n = 1):
    circlesTesting = math.ceil(pointsTesting/3)
    linesTesting = math.floor(pointsTesting/3)
    
    cols = math.ceil(math.sqrt(n))
    rows = math.ceil(n/cols)
    
    gridX = round(xPixels/cols)
    gridY = round(yPixels/rows)
    hX = round((xPixels/cols)/2)
    hY = round((yPixels/rows)/2)
    
    grid = []
    for i in range(0, cols):
        for j in range(0, rows):
            newPoint = Point(gridX/2 + (i * gridX), gridY/2 + (j * gridY))
            grid.append(newPoint)
    
        maxRadius = int(min(gridX, gridY)/2)

    for i in range(circlesTesting):
        index = i % n
        randomRadius = random.randint(1, maxRadius)
        randomPoint = Point(grid[index].x, grid[index].y)

        newCircle = Circle(randomPoint, randomRadius)
        shapes.append(newCircle)

    for i in range(linesTesting):
        index = i % n
        randomP1 = Point(random.randint(int(grid[index].x) - hX, int(grid[index].x) + hX), random.randint(int(grid[index].y) - hY, int(grid[index].y) + hY))
        while True:
          if abs(grid[index].x - randomP1.x) < 2  and abs(grid[index].y - randomP1.y) < 2:
            randomP1.x = random.randint(int(grid[index].x) - hX, int(grid[index].x) + hX)
            randomP1.y = random.randint(int(grid[index].y) - hY, int(grid[index].y) + hY)
          else:
            break
        center = grid[index]
        
        dx = center.x - randomP1.x 
        dy = center.y - randomP1.y
        magnitude = math.sqrt(dx**2 + dy**2)
        
        newPoint = Point(dx/magnitude, dy/magnitude)        
        randomP2 = Point(round(randomP1.x + (newPoint.x * (magnitude * 2))), round(randomP1.y + (newPoint.y * (magnitude* 2))))

        newLine = Line(randomP1, randomP2)
        shapes.append(newLine)
        
test_functions_overlap = {
    "polygonPolygonOverlap" : polygonPolygonFullOverlap,
    "circleCircleOverlap" : circleCircleFullOverlap,
    "lineLineOverlap" : lineLineFullOverlap,
    "aabbNoOverlap" : aabbFullOverlap,
    "circleLineOverlap" : circleLineFullOverlap
}

test_functions_grid_overlap = {
    "polygonPolygonGridOverlap" : polygonPolygonFullOverlap,
    "circleCircleGridOverlap" : circleCircleFullOverlap,
    "lineLineGridOverlap" : lineLineFullOverlap,
    "aabbGridOverlap" : aabbFullOverlap,
    "circleLineGridOverlap" : circleLineFullOverlap
}