import heapq
# Find the elf carrying the most calories. 
# And return the total calories

# Each elf's inventory is seperated by a "/n"

# with statement ensures proper closing (used for exception handling)
def day1():
   with open("input.txt","r") as data:
      # print(data.read())

      # we want to parse the data by new lines
      # and sum each group and compare for the highest calories
      maxCalories = 0
      curSum = 0
      for line in data:
         if line == "\n": # we hit a new line 
            maxCalories = max(maxCalories, curSum)
            curSum = 0
         else:
            curSum += int(line)
      maxCalories = max(maxCalories, curSum)

      print(maxCalories)
      #print(data.read().split("\n"))

# total Calories carried by the top 3 elves
def partTwo():
   with open("input.txt", "r") as data:

      calories = [] #minHeap of size 3
      curSum = 0
      # print(data.read())
      for line in data.read().split("\n"):
         if line == "": #new inventory
            heapq.heappush(calories, curSum)
            while len(calories) > 3:
               heapq.heappop(calories)
            curSum = 0
         else:
            curSum += int(line)
      heapq.heappushpop(calories,curSum) # this only works if we are guanteed to have more than 3 inventories/elves

      print(sum(calories))
partTwo()