def main():
   # figure out where the tail goes as the head follows a series of motions
   # both H T start at the same position (overlapping)

   #return the number of unique positions the tail traverses

   #Rules:
   # H - can move in the 4 cardinal directions
   # T - only needs to move if it isnt touching H
   #   If head is ever two steps away, tail must move one step in that direction
   #   If head arent touching and not in same row/col tail moves diagonal (head above or below)
   with open("test.txt", "r") as data:
      hDIRS = [(line.split()) for line in data]
      tDIRS = [(0,0), (0,1), (0,-1), (1,0), (-1,0),(1,1), (1,-1), (-1,1),(-1,-1)]
      visitedTail = part1(hDIRS, tDIRS, [0,0], [0,0])
      print(len(visitedTail))

def part1(hDIRS, tDIRS, head, tail):
   visitedTail = set(tail) # position s
   for dir, count in hDIRS:
      for i in range(int(count)):
         #move head in that direction, dir
         # then move tail in the corresponding position and add to set if not exist
         if dir == "U":
            head[0] += 1
            # if touching still dont do anything
            for dr, dc in tDIRS:
               nr, nc = head[0] + dr, head[1] + dc
               if (tail == [nr,nc]):
                  break #if one of the sides touching dont do anything for this count
            else: # runs after for loop BUT if the loop breaks, the else block is not executed.
               # THUS, we run this if there is no touching HT
               
               #if tail in the same row or col: move in that direction
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
               #else diagonal 
               else: # not in same row or col, thus diagonal
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
               visitedTail.add(tail)
               
         # elif dir == "D":

         # elif dir == "L":

         # elif dir == "R":



if __name__ == "__main__":
   main()