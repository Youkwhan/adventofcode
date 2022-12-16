# Sensors and beacons always exist at integer coord
# Each sensor knows its own position. Can determine position of one closest beacon
#There is never a tie in distance
# counting the positions where a beacon cannot possibly be along just a single row.


#find the peremeter for each sensor then 
# we look at the row if the permieter goes in that row anything in between is taken
from collections import defaultdict

#merge intervals
class Point:
 
   def __init__(self, x: int, y: int):
      self.x = x
      self.y = y
 
   def __add__(self, other):
      return (self.x + other.x, self.y + other.y)

   def delta(self, x=0, y=0):
      return Point(self.x + x, self.y + y)

   def __eq__(self, other):
      return self.x == other.x and self.y == other.y

   def __hash__(self):
      return hash(f"{self.x},{self.y}")

   def __repr__(self):
      return f"Point({self.x},{self.y})"


def part1(str_data: str, y: int):
   sensors, beacons, pairs = get_map(str_data)
   locations = set() # on row y which locations are visited

   for s, b in pairs:
      locations.update(get_marks_at_y_axis(s, b, y)) 
        # range of x-coord that sensors can detect the beacons at given y
   
   # remove the spots that are already taken by a sensor or beacon
   for s in sensors:
      if s.y == y and s.y in locations:
         locations.remove(s.x)
   
   for b in beacons:
      if b.y == y and b.y in locations:
         locations.remove(b.y)
   
   print(y, len(locations))
 
# beacon is not detected by any sensors!
# must be within x=0 up y= 4000000 lower
# tuning frequency = (x * 4000000) + y

def part2(data: str, limit_tl: Point, limit_dr: Point):
   sensors, beacons, pairs = get_map(data)
   store = defaultdict(lambda: 0)

   sensor_id = 0
   sensor_total = len(sensors)
   for sensor, beacon in pairs:
      sensor_id += 1

      dist = manhattan_distance(sensor, beacon) + 1
      print(f"{sensor_id} of {sensor_total}: sensor {sensor} with beacon {beacon} (distance={dist})")
      vertical = -1

      xmin = max(limit_tl.x, sensor.x - dist)
      xmax = min(limit_dr.x, sensor.x + dist)

      for x in range(xmin, xmax + 1):

         if x <= sensor.x:
               vertical += 1
         else:
               vertical -= 1

         cu = (x, sensor.y - vertical)
         cd = (x, sensor.y + vertical)


         if cu == cd:
               store[cu] += 1
         else:
               store[cu] += 1
               store[cd] += 1

         if store[cu] == 4:
               print(cu)

         if store[cd] == 4:
               print(cd)


 
def get_marks_at_y_axis(sensor: Point, beacon: Point, y):
   distance = manhattan_distance(sensor, beacon) # the maximum distance each sensor will go
   distance_from_axis = abs(y - sensor.y) # how far is the sensor from the given y LIMIT
   limit = max(distance - distance_from_axis, 0) # 0 if the range is included and >0 if the sensor is too far from the y-Limit
   # limit is either 0 (too far), or a number representing how much more distance after hitting the y-limit
   return set(range(sensor.x - limit, sensor.x + limit + 1)) # the range that the sensor marks at row y


def manhattan_distance(s: Point, b: Point):
   return abs(b.x - s.x) + abs(b.y - s.y)


def get_map(str_data: str):
   sensors = set()
   beacons = set()
   pairs = []

   for l in str_data.strip().split('\n'):
      pieces = (l + ';').split(' ')
      pieces_chosen = [pieces[x][:-1].split('=')[-1] for x in (2, 3, 8, 9)]
      x1, y1, x2, y2 = map(int, pieces_chosen)
      sensors.add(Point(x1, y1))
      beacons.add(Point(x2, y2))
      pairs.append((Point(x1, y1), Point(x2, y2)))

   return sensors, beacons, pairs
LIMIT_P2 = 4000000
LIMIT_P1 = 2000000
if __name__ == "__main__":
   with open("input.txt", "r") as data:
      data = data.read().strip()
      part1(data, 10)
      # part2(data, Point(0, 0), Point(LIMIT_P2, LIMIT_P2))
      print((3244277*4000000) + 2973564)
#(3244277, 2973564)
