# determine the total size of each directory.
# Sum all the directories that have a size of at most 100,000

# SOLUTION:
# we have a stack that contains all the current directory paths (states)
# if we reach a file, loop through the stack of directories and 
# update each corresponding key = directory path: val += file size

# then our hashmap will contain keys of every absolute directory paths and their file size at every moment.
# ====

# and if we find a file adding the size to all directories in our cur stack


# We only care about:
#  (cd) a change in directory
#  (ls) list of file sizes' number

from collections import defaultdict

def partOne():
   with open("input.txt", "r") as data:
      directorySize = defaultdict(int) # key= absolute paths of all directories : val=sizes (used to add file sizes to directories in stack)
      currentStack = [] # stack of all directorie's absolute path we are considering at the given time 
      currentPath = "" # current absolute path of a directory (used to push to stack)
      for line in data:
         # (cd) a change in directory
         if line.startswith("$ cd"):
            # root directory, initalize first time
            if line.strip() == "$ cd /":
               currentPath = "/"
               currentStack.append("/")

            # remove directory
            elif line.strip() == "$ cd ..":
               currentPath = "/".join(currentPath.split("/")[:-1])
               currentStack.pop()

            # add directory
            else:
               if currentPath == "/":
                  # first time we add
                  currentPath += line.split()[-1]
               else:
                  # add the last letters, $ cd A-Z
                  currentPath += f"/{line.split()[-1]}"
               currentStack.append(currentPath)
         
         # (number) a file size
         if line[0].isdigit():
            fileSize = int(line.split()[0])
            # we need to add filesize to all directories we have seen (stack) and record them in our dictionary
            for directory in currentStack:
               directorySize[directory] += fileSize
      
      output = [size for size in directorySize.values() if size <= 100000]
      print(sum(output))

#partOne()

# A filesystem has a total space of 70,000,000
# we need 30,000,000 unused space
# return the total size of the smallest directory we can delete to make enough space

def partTwo():
   with open("input.txt", "r") as data:
      directorySize = defaultdict(int) # key= absolute paths of all directories : val=sizes (used to add file sizes to directories in stack)
      currentStack = [] # stack of all directorie's absolute path we are considering at the given time 
      currentPath = "" # current absolute path of a directory (used to push to stack)
      for line in data:
         # (cd) a change in directory
         if line.startswith("$ cd"):
            # root directory, initalize first time
            if line.strip() == "$ cd /":
               currentPath = "/"
               currentStack.append("/")

            # remove directory
            elif line.strip() == "$ cd ..":
               currentPath = "/".join(currentPath.split("/")[:-1])
               currentStack.pop()

            # add directory
            else:
               if currentPath == "/":
                  # first time we add
                  currentPath += line.split()[-1]
               else:
                  # add the last letters, $ cd A-Z
                  currentPath += f"/{line.split()[-1]}"
               currentStack.append(currentPath)
         
         # (number) a file size
         if line[0].isdigit():
            fileSize = int(line.split()[0])
            # we need to add filesize to all directories we have seen (stack) and record them in our dictionary
            for directory in currentStack:
               directorySize[directory] += fileSize
      
      unused = 70000000 - directorySize["/"]
      need = 30000000 - unused
      output = [size for size in directorySize.values() if size >= need]
      print(output)
      print(min(output))
partTwo()