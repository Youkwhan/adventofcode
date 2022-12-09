# crates need to be unloaded = supplies
# cargo crane = stack
from collections import defaultdict, deque
def partOne():
   # return the combine string of all the top crates in each stack
   # hashmap adjList of each stack
   #then read the move procedures and pop/append
   with open("input.txt", "r") as data:
      data = data.read()
      
      stacks, moves = data.split("\n\n") # double empty line, so we split the stacks and moves instructions
      stacks = stacks.split("\n") # list of stack row by row
      
      rows = stacks[:-1] # except the last
      cols = stacks[-1] # the last ['1' '2' '3']
      adjList = defaultdict(deque)

      # Go through stacks and create a adjList
      for row in rows: # for each row of the stack
         for i in range(1,len(row),4):# char coresponding to an index each 3 apart
            #print(row[i], i//4)
            if row[i] != " ":
               adjList[str((i//4)+1)].appendleft(row[i])
      #print(adjList) # {col: [bot, ..., top] }

      # Go through the instructions 
      moves = moves.split("\n")
      for move in moves:
         # move = [move 1 from 2 to 1] loop 1 times pop from 2 -> push 1
         move = move.split()
         count = int(move[1]) #how many times
         remove = move[3] # remove from
         add = move[5] # add to

         while count:
            tmp = adjList[remove].pop()
            adjList[add].append(tmp)
            count -= 1
      #print(adjList)

      # Get our result top of our stack
      output = sorted([(key, val[-1]) for key, val in adjList.items()])
      output = "".join([tuple[1] for tuple in output])
      print(output)

def partTwo():
   # we now have CrateMover 9001 which has a new feature of moving multiple crates at once
   with open("input.txt", "r") as data:
      data = data.read()
      
      stacks, moves = data.split("\n\n") # double empty line, so we split the stacks and moves instructions
      stacks = stacks.split("\n") # list of stack row by row
      
      rows = stacks[:-1] # except the last
      cols = stacks[-1] # the last ['1' '2' '3']
      adjList = defaultdict(deque)

      # Go through stacks and create a adjList
      for row in rows: # for each row of the stack
         for i in range(1,len(row),4):# char coresponding to an index each 3 apart
            #print(row[i], i//4)
            if row[i] != " ":
               adjList[str((i//4)+1)].appendleft(row[i])
      #print(adjList) # {col: [bot, ..., top] }

      # Go through the instructions 
      moves = moves.split("\n")
      for move in moves:
         # move = [move 1 from 2 to 1] loop 1 times pop from 2 -> push 1
         move = move.split()
         count = int(move[1]) #how many crates to move
         remove = move[3] # remove from
         add = move[5] # add to

         # pop multiple crates
         tmp = []
         while count:
            tmp.append(adjList[remove].pop())
            count -= 1
         adjList[add].extend(reversed(tmp))
        
      #print(adjList)

      # Get our result top of our stack
      output = sorted([(key, val[-1]) for key, val in adjList.items()])
      output = "".join([tuple[1] for tuple in output])
      print(output)

partTwo()