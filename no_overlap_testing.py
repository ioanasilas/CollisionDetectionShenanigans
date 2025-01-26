import random
import math
from shapes import Point, Polygon, Circle, Line, Rectangle
from shared_data import shapes, pointsTestingDict

xPixels = 1024
yPixels = 618
density = 0.5

# Nonoverlapping points generation

def circleCircleNonOverlap(pointsTesting):
    shapesTesting = pointsTesting

    n = shapesTesting
    
    cols = math.ceil(math.sqrt(n))
    rows = math.ceil(n/cols)
    
    gridX = round(xPixels/cols)
    gridY = round(yPixels/rows)
    
    grid = []
    
    for i in range(0, cols):
        for j in range(0, rows):
            newPoint = Point(gridX/2 + (i * gridX), gridY/2 + (j * gridY))
            grid.append(newPoint)
            
    maxRadius = int(min(gridX, gridY)/2) - 1
    hR = int(maxRadius/2)

  # we want shapesTesting many points
    for i in range(0, shapesTesting):
        randomRadius = random.randint(hR, maxRadius)
        randomPoint = Point(grid[i].x, grid[i].y)

        newCircle = Circle(randomPoint, randomRadius)
        shapes.append(newCircle)

def aabbNoOverlap(pointsTesting):
    # this does NOT work,
    # I actually do not know why
    # see debug.. please
    shapesTesting = int(pointsTesting/2)

    n = shapesTesting
    
    cols = math.ceil(math.sqrt(n))
    rows = math.ceil(n/cols)
    
    gridX = int(xPixels/cols)
    gridY = int(yPixels/rows)
    hX = round((xPixels/cols)/2) - 1
    hY = round((yPixels/rows)/2) - 1
    
    grid = []
    
    for i in range(0, cols):
        for j in range(0, rows):
            newPoint = Point(gridX/2 + (i * gridX), gridY/2 + (j * gridY))
            grid.append(newPoint)

    for i in range(shapesTesting):
        randomP1 = Point(random.randint(int(grid[i].x) - hX, int(grid[i].x)), random.randint(int(grid[i].y) - hY, int(grid[i].y)))
        randomP2 = Point(random.randint(int(grid[i].x), int(grid[i].x) + hX), random.randint(int(grid[i].y), int(grid[i].y) + hY))

        newBox = Rectangle(randomP1, randomP2)
        shapes.append(newBox)


def lineLineNoOverlap(pointsTesting):
    shapesTesting = int(pointsTesting / 2)
    
    n = shapesTesting
    
    cols = math.ceil(math.sqrt(n))
    rows = math.ceil(n/cols)
    
    gridX = round(xPixels/cols)
    gridY = round(yPixels/rows)
    hX = round((xPixels/cols)/2) - 1
    hY = round((yPixels/rows)/2) - 1
    
    grid = []
    for i in range(0, cols):
        for j in range(0, rows):
            newPoint = Point(gridX/2 + (i * gridX), gridY/2 + (j * gridY))
            grid.append(newPoint)
            
    for i in range(shapesTesting): 
        randomP1 = Point(random.randint(int(grid[i].x) - hX, int(grid[i].x) + hX), random.randint(int(grid[i].y) - hY, int(grid[i].y) + hY))
        while True:
          if abs(grid[i].x - randomP1.x) < 2  and abs(grid[i].y - randomP1.y) < 2:
            randomP1.x = random.randint(int(grid[i].x) - hX, int(grid[i].x) + hX)
            randomP1.y = random.randint(int(grid[i].y) - hY, int(grid[i].y) + hY)
          else:
            break
                 
        center = grid[i]
        
        dx = center.x - randomP1.x 
        dy = center.y - randomP1.y
        magnitude = math.sqrt(dx**2 + dy**2)
        
        newPoint = Point(dx/magnitude, dy/magnitude)        
        randomP2 = Point(round(randomP1.x + (newPoint.x * (magnitude * 2))), round(randomP1.y + (newPoint.y * (magnitude* 2))))

        newLine = Line(randomP1, randomP2)
        shapes.append(newLine)

def polygonPolygonNoOverlap(pointsTesting):
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
    n = shapesTesting
    
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
    # leftover_points = pointsTesting % num_edges
    
    i = 0
    for edgesInPolygon in edgeNumArr:
        randomPosX = int(grid[i].x)
        randomPosY = int(grid[i].y)
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
        
        shapes.append(translated_polygon)
        i += 1

    # print(polygons)
    # print(num_edges)
    # print(no_of_polys)

    # Add every polygon to shapes


def circleLineNoOverlap(pointsTesting):
    circlesTesting = math.ceil(pointsTesting/3)
    linesTesting = math.floor(pointsTesting/3)

    toGenerate = []
    for i in range(circlesTesting):
      toGenerate.append(0)
    for i in range(linesTesting):
      toGenerate.append(1)
    
    n = circlesTesting + linesTesting
    
    cols = math.ceil(math.sqrt(n))
    rows = math.ceil(n/cols)
    
    gridX = round(xPixels/cols)
    gridY = round(yPixels/rows)
    hX = round((xPixels/cols)/2) - 1
    hY = round((yPixels/rows)/2) - 1
    
    grid = []
    for i in range(0, cols):
        for j in range(0, rows):
            newPoint = Point(gridX/2 + (i * gridX), gridY/2 + (j * gridY))
            grid.append(newPoint)
    
    maxRadius = int(min(gridX, gridY)/2) - 1
    hR = int(maxRadius/2)

    for i in range(n):
      randomIndex = random.randint(0, len(toGenerate) - 1)
      if toGenerate.pop(randomIndex) == 0:
        randomRadius = random.randint(hR, maxRadius)
        randomPoint = Point(grid[i].x, grid[i].y)

        newCircle = Circle(randomPoint, randomRadius)
        shapes.append(newCircle)
      else:
        randomP1 = Point(random.randint(int(grid[i].x) - hX, int(grid[i].x) + hX), random.randint(int(grid[i].y) - hY, int(grid[i].y) + hY))
        while True:
          if abs(grid[i].x - randomP1.x) < 2  and abs(grid[i].y - randomP1.y) < 2:
            randomP1.x = random.randint(int(grid[i].x) - hX, int(grid[i].x) + hX)
            randomP1.y = random.randint(int(grid[i].y) - hY, int(grid[i].y) + hY)
          else:
            break
          
        center = grid[i]
        
        dx = center.x - randomP1.x 
        dy = center.y - randomP1.y
        magnitude = math.sqrt(dx**2 + dy**2)
        
        newPoint = Point(dx/magnitude, dy/magnitude)        
        randomP2 = Point(round(randomP1.x + (newPoint.x * (magnitude * 2))), round(randomP1.y + (newPoint.y * (magnitude* 2))))

        newLine = Line(randomP1, randomP2)
        shapes.append(newLine)
        
test_functions_no_overlap = {
    "polygonPolygonNoOverlap" : polygonPolygonNoOverlap,
    "circleCircleNoOverlap" : circleCircleNonOverlap,
    "lineLineNoOverlap" : lineLineNoOverlap,
    "aabbNoOverlap" : aabbNoOverlap,
    "circleLineNoOverlap" : circleLineNoOverlap
}