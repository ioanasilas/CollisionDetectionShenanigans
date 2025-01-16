import math
import pygame

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    # get coordinates
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def __sub__ (self, other):
        return Point(self.x - other.x, self.y - other.y)
  
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def inPolygon(self, polygon): #this is baiscally raycasting
        n = len(polygon.points)
        intersections = 0

        for i in range(n):
            # go thru polygon edges
            p1 = polygon.points[i]
            p2 = polygon.points[(i + 1) % len(polygon.points)]

            # ensure that edge crosses ray's horizontal line
            # one vertex above, one below
            if (p1.y > self.y) != (p2.y > self.y):
                # linear interpolation, we assume horizontal ray
                intersect_x = p1.x + (self.y - p1.y) * (p2.x - p1.x) / (p2.y - p1.y)
                # if intersection to the rigt of point, it's valid, increase count
                if intersect_x > self.x:
                    intersections += 1
        # we do not find exact intersection point
        # just determine where it is
        return (intersections % 2 == 1) #even = outside, odd = inside

class Shape:
    def __init__(self, name):
        self.name = 'Shape'
        self.intersecting = False

    # move by changing x and y coords
    # what is position?
    def move(self, dx, dy):
        self.position.x = dx
        self.position.y = dy

class Polygon(Shape):
  def __init__(self, points):
    # calls shape constructor
    super().__init__("Polygon")
    self.points = points
    self.edges = self.compute_edges()
    self.normals = self.compute_normals()

  def __repr__(self):
        return f"Polygon with points: {', '.join([repr(p) for p in self.points])}"

  # SAT
  def compute_edges(self):
    # compute edges as vectors between consecutive vertices
    edges = []
    for i in range(len(self.points)):
      p1 = self.points[i]
      p2 = self.points[(i + 1) % len(self.points)] # we wrap to first point when we run out
      edges.append(p2 - p1)
    return edges
    
  def compute_normals(self):
    # compute perpendicular vectors of the edges
    normals = []
    for edge in self.edges:
      normal = Point(-edge.y, edge.x) # rotate vector by 90 degrees
      # get length of a vector using pythagorean theorem
      length = math.hypot(normal.x, normal.y)
      # make vector's length equal 1 but keep direction unchanged
      # we do not care about length in sat, only direction is needed for projection
      normals.append(Point(normal.x / length, normal.y / length))
    return normals

  def project_onto_axis(self, axis):
    # project polygon onto normal vector, creating shadow
    # shadow is important since if shadows of two polyons on an axis do not overlap, then the polygons are NOT colliging
    # if they overlap on ALL axes, they are colliding
    # we make min and max initially equal to first point's projection
    min_projection = max_projection = self.points[0].x * axis.x + self.points[0].y * axis.y
    # then go through the others
    for point in self.points[1:]:
      # project point onto axis by calculating dot product
      projection = point.x * axis.x + point.y * axis.y
      # update minimum and max projection
      min_projection = min(min_projection, projection)
      max_projection = max(max_projection, projection)
    # return the range, which is te start and end of the shadow
    return min_projection, max_projection
  
  def intersects(self, other):
    if type(other) == Polygon:
        # check for collision using SAT
        for normal in self.normals + other.normals:
            projection1_min, projection1_max = self.project_onto_axis(normal)
            projection2_min, projection2_max = other.project_onto_axis(normal)
            if projection1_max < projection2_min or projection2_max < projection1_min:
                return False # found separating axis so no collision
        return True # no separating axis, collision detected
    
    elif type(other) == Circle:
        return polygonCircleCollision(self, other)
    elif type(other) == Line:
        return polygonLineCollision(self, other)
  
  def draw(self, screen, color, outline = 0):
      pygame.draw.polygon(screen, color, [(p.x, p.y) for p in self.points], outline)
    
#   def __repr__(self):
#     return f"Point({self.x}, {self.y})"
  
  def move(self, dx, dy):
    for point in self.points:
      point.x += dx
      point.y += dy

class Rectangle(Shape):
    def __init__(self, min_point, max_point):
        super().__init__("Rectangle")
        self.min_point = Point(min(min_point.x, max_point.x), min(min_point.y, max_point.y))
        self.max_point = Point(max(min_point.x, max_point.x), max(min_point.y, max_point.y))

    ## AABB
    def intersects(self, other):
        xAxisIntersect = False
        yAxisIntersect = False
        if (self.min_point.x <= other.max_point.x and self.max_point.x >= other.min_point.x):
            xAxisIntersect = True
        if (self.min_point.y <= other.max_point.y and self.max_point.y >= other.min_point.y):
            yAxisIntersect = True
        return xAxisIntersect and yAxisIntersect  # Returns True or False
    
    def move(self, dx, dy):
        self.min_point.x += dx
        self.min_point.y += dy
        self.max_point.x += dx
        self.max_point.y += dy

    def draw(self, screen, color, outline = 0):
        pygame.draw.rect(screen, color, pygame.Rect(self.min_point.x, self.min_point.y, self.max_point.x - self.min_point.x, self.max_point.y - self.min_point.y), outline)

# circle circle
class Circle(Shape):
    def __init__(self, position, radius):
        super().__init__("Circle")
        self.position = position
        self.radius = radius

    def move(self, dx, dy):
        self.position.x += dx
        self.position.y += dy

    def intersects(self, other):
        if type(other) == Circle:
            # get distance between 2 circles
            distance = math.sqrt((other.position.x - self.position.x)**2 + (other.position.y - self.position.y)**2)
            # if dist is less than sum of radiuses, they intersect
            return distance <= (self.radius + other.radius)
        elif type(other) == Line:
            return circleLineCollision(self, other)
        elif type(other) == Polygon:
            return polygonCircleCollision(other, self)
        
    def draw(self, screen, color, outline = 0):
        pygame.draw.circle(screen, color, (self.position.x, self.position.y), self.radius, outline)        

# Line Line
class Line(Shape):
    def __init__(self, point1, point2):
        super().__init__("Line")
        self.point1 = point1
        self.point2 = point2

    def move(self, dx, dy):
        self.point1.x += dx
        self.point2.x += dx
        self.point1.y += dy
        self.point2.y += dy
    
    def getSize(self):
        return math.sqrt((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2)

    def intersects(self, other):
        if type(other) == Line:
            # line1
            x1, y1 = self.point1.x, self.point1.y
            x2, y2 = self.point2.x, self.point2.y
            # line2
            x3, y3 = other.point1.x, other.point1.y
            x4, y4 = other.point2.x, other.point2.y
            
            # if 0, lines are parallel or coincident, no intersect
            denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

            if denominator == 0:
                return None

            # intersection parameters
            # t determines intersection point on line1, u on line2
            # this is from point on line equations then cramer s rule
            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
            u = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / denominator

            # if intersection lies on both line segments
            if 0 <= t <= 1 and 0 <= u <= 1:
                intersection_x = x1 + t * (x2 - x1)
                intersection_y = y1 + t * (y2 - y1)
                return Point(intersection_x, intersection_y)

            return None
        
        elif type(other) == Polygon:
            return polygonLineCollision(other, self)
        elif type(other) == Circle:
            return circleLineCollision(other, self)
    
    def draw(self, screen, color, outline = 5):
        pygame.draw.line(screen, color, (self.point1.x, self.point1.y), (self.point2.x, self.point2.y), outline)

def circleLineCollision(circle, line):
    # circle center
    cx, cy = circle.position.x, circle.position.y
    # first and end point of line
    x1, y1 = line.point1.x, line.point1.y
    x2, y2 = line.point2.x, line.point2.y

    #Distances
    dx = x2 - x1 
    dy = y2 - y1
    cdx = cx - x1
    cdy = cy - y1

    denominator = (dx**2 + dy**2)
    # if lines endpoints coincide
    if denominator == 0:
        # if line is a point, check distance from circle center to it
        distance = math.sqrt(cdx**2 + cdy**2)
        return distance <= circle.radius

    #if t is less than 0, the closest point is beyond x1, y1, 
    # and if t is greater than 1, the closest point is beyond x2, y2
    t = max(0, min(1, (cdx * dx + cdy * dy)/denominator))

    # x, y coordinates of closest points on line
    closest_x = x1 + (t * dx)
    closest_y = y1 + (t * dy)

    # distance between circle center and closest point on line
    distance = math.sqrt((closest_x - cx)**2 + (closest_y - cy)**2)
    return distance <= circle.radius
    
def polygonLineCollision(polygon, line):
    for i in range(len(polygon.points)):
        # we apply LineLine multiple times, for each edge
        l = Line(polygon.points[i], polygon.points[(i + 1) % len(polygon.points)])
                
        collides = line.intersects(l)
        if collides:
            return collides
    
    # this is raycasting, to also check for intersection inside polygon
    if line.point1.inPolygon(polygon): #will have to be changed if we use polygons with holes
        return True
        
def polygonCircleCollision(polygon, circle):
    for i in range(len(polygon.points)):
        # we get every line and check if it collides with the circle
        l = Line(polygon.points[i], polygon.points[(i + 1) % len(polygon.points)])
                
        collides = circleLineCollision(circle, l)
        if collides:
            return collides
    
    # this is raycasting, to also check for intersection inside polygon
    if circle.position.inPolygon(polygon):
        return True