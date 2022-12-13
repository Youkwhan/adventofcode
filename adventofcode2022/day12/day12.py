# a is the lowest elevation, to the highest elevation, z.
# Your current position (S) has elevation a,
# best signal (E) has elevation z

# Objective: get to position E in the fewest steps 

# step: 4 cordinal, only 1 elevation higher
import collections
def main():
   with open("input.txt", "r") as data:
      grid = [list(line.strip()) for line in data]
      ROWS, COLS = len(grid), len(grid[0])
      DIR = [(0,1), (1,0), (0,-1), (-1,0)]

      # DONT RUN BOTH at the same time since we are mutating the original grid
      #part1(grid, ROWS, COLS, DIR)
      print(part2(grid, ROWS, COLS, DIR))


def part1(grid, ROWS, COLS, DIR):
   q = collections.deque()
   visited = set()
   steps = 0
   E = (0,0)

   for r in range(ROWS):
      for c in range(COLS):
         if grid[r][c] == "S":
            q.append((r,c))
            visited.add((r,c))
            grid[r][c] = "a"
         if grid[r][c] == "E":
            E = (r,c)
            grid[r][c] = "z"

   while q:
      for _ in range(len(q)):
         r, c = q.popleft()
         if (r,c) == E:
               return steps
         for dr, dc in DIR:
            nr, nc = dr + r, dc + c
            if (nr < 0 or nr >= ROWS or
            nc < 0 or nc >= COLS or
            (nr,nc) in visited or
            ord(grid[nr][nc]) - ord(grid[r][c]) > 1):
               continue
            
            visited.add((nr,nc))
            q.append((nr,nc))
      steps += 1
   return steps
   
def part2(grid, ROWS, COLS, DIR):
   # maximize exercise while taking the shortest route (want to start at a)
   # goal is E
   q = collections.deque()
   visited = set()
   E = tuple
   steps = 0

   for r in range(ROWS):
      for c in range(COLS):
         if grid[r][c] == "S":
            grid[r][c] = "a"
            q.append((r,c))
            visited.add((r,c))
         elif grid[r][c] == "a":
            q.append((r,c))
            visited.add((r,c))
         elif grid[r][c] == "E":
            E = (r,c)
            grid[r][c] = "z"

   while q:
      #level
      for _ in range(len(q)):
         r, c = q.popleft()
         if (r,c) == E:
            return steps
         
         for dr, dc in DIR:
            nr, nc = dr + r, dc + c
            if (nr < 0 or nr >= ROWS or
               nc < 0 or nc >= COLS or 
               (nr,nc) in visited or
               ord(grid[nr][nc]) - ord(grid[r][c]) > 1):
               continue

            visited.add((nr,nc))
            q.append((nr,nc))

      # we increment step first and then Look at the surroundings
      steps += 1
   return steps




if __name__ == "__main__":
   main()