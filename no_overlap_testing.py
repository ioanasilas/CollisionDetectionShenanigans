import random
import math
from shapes import Point, Polygon, Circle, Line, Rectangle
from shared_data import shapes


xPixels = 1024
yPixels = 618
pointsTesting = 50
density = 1

# Nonoverlapping points generation

def circleCircleNonOverlap():
    shapesTesting = pointsTesting
    avgRadius = int(math.sqrt((density * (xPixels * yPixels))/(math.pi * shapesTesting)))
    hR = int(avgRadius/2)

  # we want shapesTesting many points
    for i in range(0, shapesTesting):
        while(True): # keep trying until a valid circle in generated
          randomRadius = random.randint(avgRadius - hR, avgRadius + hR)
          randomPoint = Point(random.randint(0 + randomRadius, xPixels - randomRadius), random.randint(0 + randomRadius, yPixels - randomRadius))

          newCircle = Circle(randomPoint, randomRadius)

          is_overlapping = False
          # check if overlapping any shape that is already there
          for shape in shapes:
            if isinstance(shape, Circle):
              dist = math.sqrt((newCircle.position.x - shape.position.x)**2 + (newCircle.position.y - shape.position.y)**2)
            if dist < newCircle.radius + shape.radius:
              is_overlapping = True
              break
          
          if not is_overlapping:
            # add circle if it ok
            shapes.append(newCircle)
            break

def aabbNoOverlap():
    # this does NOT work,
    # I actually do not know why
    # see debug.. please
    shapesTesting = int(pointsTesting/2)
    avgSize = int(math.sqrt((density * (xPixels * yPixels))/(shapesTesting)))
    hS = int(avgSize/2)
    sizeRange = avgSize + hS

    print(f"Shapes to generate: {shapesTesting}, Size range: {sizeRange}")


    for i in range(shapesTesting):
        while(True):
          randomP1 = Point(random.randint(0, xPixels - sizeRange), random.randint(0, yPixels - sizeRange))
          randomP2 = Point(random.randint(randomP1.x + hS, randomP1.x + sizeRange), random.randint(randomP1.y + hS, randomP1.y + sizeRange))
          print(f"Trying rectangle at ({randomP1}, {randomP2})")

          newBox = Rectangle(randomP1, randomP2)
          is_overlapping = False
          for shape in shapes:
             if isinstance(shape, Rectangle):
                # don t we just check if we collide?
                # and we do this.. with.. AABB? too cursed?
                if newBox.intersects(shape):
                   is_overlapping = True
                   print(f"Not adding {newBox} to shapes")
                   break
                
          if not is_overlapping:
            shapes.append(newBox)
            print(f"Adding {newBox} to shapes")
            break

# def lineLineRandom():
#     shapesTesting = int(pointsTesting / 2)
#     avgLength = int(math.sqrt((density * (xPixels * yPixels)) / shapesTesting))
#     lengthRange = int(avgLength*2)

#     for i in range(shapesTesting):
#         randomP1 = Point(random.randint(0, xPixels), random.randint(0, yPixels))
#         randomP2 = Point(
#             max(0, min(xPixels, randomP1.x + random.randint(-lengthRange, lengthRange))),
#             max(0, min(yPixels, randomP1.y + random.randint(-lengthRange, lengthRange))),
#         )

#         newLine = Line(randomP1, randomP2)
#         shapes.append(newLine)

# def polygonPolygonRandom():
#     points_used = 0
#     shapesTesting = 0
#     maxEdges = 10

#     edgeNumArr = []
    
#     while points_used < pointsTesting:
#         #print(points_used)
#         if points_used >= pointsTesting - (maxEdges + 3):
#             if points_used < pointsTesting - 5:
#                 num_edges = random.randint(3, pointsTesting - (points_used + 3))
#                 edgeNumArr.append(num_edges)
#                 points_used += num_edges
            
#             edgeNumArr.append(pointsTesting - points_used)
#             points_used += pointsTesting - points_used
#             shapesTesting += 1
#         else:
#             num_edges = random.randint(3, 10)
#             edgeNumArr.append(num_edges)
#             points_used += num_edges

#         shapesTesting += 1

#     # print(shapesTesting, points_used)
#     # each poly has between 3 and 10 edges
#     # get how many polys we will get
#     avgSize = int(math.sqrt((density * (xPixels * yPixels))/(shapesTesting)))
#     hS = int(avgSize/2)
#     sizeRange = int(avgSize + hS)
#     # leftover_points = pointsTesting % num_edges

#     polygons = []

#     for edgesInPolygon in edgeNumArr:
#         # we can use Valtr algorithm
#         randomPosX = random.randint(hS, xPixels - hS)
#         randomPosY = random.randint(hS, yPixels - hS)
#         X = random.sample(range(randomPosX - hS, randomPosX+hS), edgesInPolygon) 
#         Y = random.sample(range(randomPosY - hS, randomPosY+hS), edgesInPolygon) 

#         # sort X, Y to get min, max
#         X.sort()
#         Y.sort()

#         minX, maxX = X[0], X[-1]
#         minY, maxY = Y[0], Y[-1]

#         # get rid of min and max
#         X1 = X[1:-1]
#         Y1 = Y[1:-1]

#         # divide remaining into 2 groups
#         xVec = []
#         yVec = []

#         lastTop = minX
#         lastBot = minX

#         for x in X1:  # Loop through X1 to calculate differences
#             if bool(random.getrandbits(1)):
#                 xVec.append(x - lastTop)  # add dif to xVec
#                 lastTop = x  # update lastTop to current x coord
#             else:
#                 xVec.append(lastBot - x)
#                 lastBot = x

#         # Close the shape by adding final points
#         xVec.append(maxX - lastTop)
#         xVec.append(lastBot - maxX)

#         lastTop = minY
#         lastBot = minY

#         for y in Y1:  # Loop through Y1 to calculate differences
#             if bool(random.getrandbits(1)):
#                 yVec.append(y - lastTop)  # add dif to yVec
#                 lastTop = y  # update lastTop to current y coord
#             else:
#                 yVec.append(lastBot - y)
#                 lastBot = y

#         # Close the shape by adding final points
#         yVec.append(maxY - lastTop)
#         yVec.append(lastBot - maxY)

#         # Shuffle points together
#         points = list(zip(xVec, yVec))
#         random.shuffle(points)

#         # Create vectors with shuffled coordinates
#         vectors = [Point(x, y) for x, y in points]

#         # Sort vectors by angle
#         vectors.sort(key=lambda v: math.atan2(v.y, v.x))

#         # Lay the points end to end
#         x, y = 0, 0
#         minPolX, minPolY = 0, 0
#         polygon_points = []

#         for v in vectors:
#             polygon_points.append(Point(x, y))
#             x += v.getX()
#             y += v.getY()

#             minPolX = min(minPolX, x)
#             minPolY = min(minPolY, y)

#         # move polygon to original min/max coordinates
#         xShift = minX - minPolX
#         yShift = minY - minPolY
#         translated_polygon = Polygon([Point(p.x + xShift, p.y + yShift) for p in polygon_points])

#         polygons.append(translated_polygon)

#     # print(polygons)
#     # print(num_edges)
#     # print(no_of_polys)

#     # Add every polygon to shapes
#     shapes.extend(polygons)


# def circleLineRandom():
#     circlesTesting = math.ceil(pointsTesting/3)
#     linesTesting = math.floor(pointsTesting/3)
    
#     avgRadius = int(math.sqrt((density * (xPixels * yPixels))/(math.pi * circlesTesting)))
#     hR = int(avgRadius/2)

#     for i in range(circlesTesting):
#         randomRadius = random.randint(avgRadius - hR, avgRadius + hR)
#         randomPoint = Point(random.randint(0 + randomRadius, xPixels - randomRadius), random.randint(0 + randomRadius, yPixels - randomRadius))

#         newCircle = Circle(randomPoint, randomRadius)
#         shapes.append(newCircle)

#     avgLength = int(math.sqrt((density * (xPixels * yPixels)) / linesTesting))
#     lengthRange = int(avgLength)

#     for i in range(linesTesting):
#         randomP1 = Point(random.randint(0, xPixels), random.randint(0, yPixels))
#         randomP2 = Point(
#             max(0, min(xPixels, randomP1.x + random.randint(-lengthRange, lengthRange))),
#             max(0, min(yPixels, randomP1.y + random.randint(-lengthRange, lengthRange))),
#         )

#         newLine = Line(randomP1, randomP2)
#         shapes.append(newLine)
