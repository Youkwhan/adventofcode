# distress signal from batcave
# sand trap!
# air + rock = sand gaps

# ROCK class?
# x,y : distance to right, distance down (rock structure)
#origin = (500, 0)

# sand produce one per unit of time.
# SAND CLASS?
# sand always falls down one step.
#  If blocked by (rock or sand), we go diagonal; left, then right
#  If no more position REST

# How many units of sand come to rest before sand starts flowing into the abyss?

#SOLUTION:
# 1. rock class that holds and generate the grid OR dictionary
# 2. sand class how each sand moves
# 3. sandTraversal function how they act together/ 
# 4. check abyss

#1. store the rock coords
#2. sand inherits a rock since once a sand stops moving it becomes a rock
#3. 
# class Sand:
#    def __init__(self, x, y):
#       self.x = x
#       self.y = y
#       self.is_moving = True
#       self.rock = None 
   
#    def move(self):
#       if self.is_moving:
#          self.y += 1
   
#    def stop(self):
#       self.is_moving = False
   
#    def turn_into_rock(self):
#       self.rock = Rock(self.x, self.y)
   
# class Rock:
#    def __init__(self, x, y) -> None:
#       self.x = x
#       self.y = y


def main():
   with open("input.txt", "r") as data:
      rock_cords = set(parse_rock_path(data)) # set takes in an iterable item\
      rock_len = len(rock_cords)
      bottom = max(y for x, y in rock_cords) + 2
      print(fill(rock_cords, bottom, bottom - 1) - rock_len)
      print(fill(rock_cords, bottom, bottom + 1) - rock_len + 1)

def drop(rock_cords, bottom, void):
   x = 500
   for y in range(void):
      for dx in (0, -1, 1):
         if (x + dx, y + 1) not in rock_cords and y + 1 != bottom:
            x += dx
            break
      else:
         return x, y

def fill(rock_cords, bottom, void):
   pos = drop(rock_cords, bottom, void)
   while pos and pos != (500, 0):
      rock_cords.add(pos)
      pos = drop(rock_cords, bottom, void)
   return len(rock_cords)   

def parse_rock_path(data): #generate itertor of coords 
   # for each line
   for line in data:
      # get a list of rock path as a tuple(int)
      rock_path = [tuple(map(int,rock_cord.split(","))) for rock_cord in line.split(" -> ")]
      # we generate a list of all rocks in that path
      for i in range(len(rock_path) -1): # compare two pairs at a time, thus -1 last pair
         (startx, starty), (endx, endy) = sorted(rock_path[i:i + 2]) # order the two pairs we are looking at

         for x in range(startx, endx + 1):
            for y in range(starty, endy + 1):
               #generate every coords from (start coord) to (end coord)
               yield x, y # generator return an "iterator" by using the encapsulated next() method

if __name__ == "__main__":
   main()


