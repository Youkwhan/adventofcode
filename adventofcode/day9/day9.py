   # figure out where the tail goes as the head follows a series of motions
   # both H T start at the same position (overlapping)

   #return the number of unique positions the tail traverses

   #Rules:
   # H - can move in the 4 cardinal directions
   # T - only needs to move if it isnt touching H
   #   If head is ever two steps away, tail must move one step in that direction
   #   If head arent touching and not in same row/col tail moves diagonal (head above or below)
def main():
   with open("input.txt", "r") as data:
      hDIRS = [(line.split()) for line in data]
      tDIRS = [(0,0), (0,1), (0,-1), (1,0), (-1,0),(1,1), (1,-1), (-1,1),(-1,-1)]
      #visitedTail = part1(hDIRS, tDIRS, [0,0], [0,0])
      visitedTail = part2(hDIRS, tDIRS, [[0,0] for i in range(10)])
      print(visitedTail)
      print(len(visitedTail))

def part1(hDIRS, tDIRS, head, tail):
   visitedTail = set([tuple(tail)]) # position s
   for dir, count in hDIRS:
      for _ in range(int(count)):
         # move head in that direction, dir
         # then move tail in the corresponding position and add to set if not exist
         if dir == "U":
            # update head
            head[0] += 1
            moveTail(tDIRS, head, tail, visitedTail)

         elif dir == "D":
            head[0] -= 1
            moveTail(tDIRS, head, tail, visitedTail)

         elif dir == "L":
            head[1] -= 1
            moveTail(tDIRS, head, tail, visitedTail)

         elif dir == "R":
            head[1] += 1
            moveTail(tDIRS, head, tail, visitedTail)

   return visitedTail

# move the tail in respect to the given head
def moveTail(tDIRS, head, tail, visitedTail, pos=8): #default 8 for part1?
   # check head surrounding; is tail touching
   for dr, dc in tDIRS:
      nr, nc = head[0] + dr, head[1] + dc
      if (tail == [nr,nc]):
         return # touching so tail doesnt move
  
   # IF NO TOUCHING 
   #if tail in the same row or col: move in that direction
   if not checkRowCol(tail, head):
   #else diagonal 
      checkDiagonal(tail,head)
   # part1:
   #visitedTail.add(tuple(tail))
   # part 2:
   if pos == 8:
      #meaning current head = 8, tail = 9
      visitedTail.add(tuple(tail))

# check row and col and move Tail in respect to head
def checkRowCol(tail, head):
   if tail[0] == head[0]:
      if tail[1] < head[1]: # head right side
         tail[1] += 1
      else: # head left side
         tail[1] -= 1
   elif tail[1] == head[1]:
      if tail[0] < head[0]: # head top side
         tail[0] += 1
      else:
         tail[0] -= 1
   else:
      return False
   return True

# move tail diagonal in respect to head position
def checkDiagonal(tail,head):
   # can only be in 4 quadrants
   # q1 = hRow > tRow, hCol < tCol
   if head[0] > tail[0] and head[1] < tail[1]:
      tail[0] += 1
      tail[1] -= 1 
   # q2 = hRow > tRow, hCol > tCol
   elif head[0] > tail[0] and head[1] > tail[1]:
      tail[0] += 1
      tail[1] += 1
   # q3 = hRow < tRow, hCol < tCol
   elif head[0] < tail[0] and head[1] < tail[1]:
      tail[0] -= 1
      tail[1] -= 1
   # q4 = hRow < tRow, hCol > tCol
   elif head[0] < tail[0] and head[1] > tail[1]:
      tail[0] -= 1
      tail[1] += 1

# now we have 10 knots (H...9)
# how many positions does the tail end of the rope visit
def part2(hDIRS, tDIRS, tails):
   # every time the head moves all of our other tails need to be updated
   visitedTail = set([(0,0)]) # position s
   for dir, count in hDIRS:
      for _ in range(int(count)):
         for i in range(len(tails)-1):
            
            head = tails[i]

            if dir == "U":
               if i == 0:
                  head[0] += 1            
               moveTail(tDIRS, head, tails[i+1], visitedTail, i)
            elif dir == "D":
               if i == 0:
                  head[0] -= 1
               moveTail(tDIRS, head, tails[i+1], visitedTail, i)
            elif dir == "L":
               if i == 0:
                  head[1] -= 1
               moveTail(tDIRS, head, tails[i+1], visitedTail, i)
            elif dir == "R":
               if i == 0:
                  head[1] += 1
               moveTail(tDIRS, head, tails[i+1], visitedTail, i)
   return visitedTail
          


if __name__ == "__main__":
   main()