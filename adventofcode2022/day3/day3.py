# we need to rearrange a few items
# All items of a given type is meant to go in either 1st or 2nd compartment
# failed to follow rule for exactly one item per rucksack

#each line = rucksack
# first compartment/2 + second compartment/2 = len(rucksack)
#sum of all the failed item per rucksack

# we need to find the dup in each line
# and calculate their priority 

def partOne():
   with open("input.txt", "r") as data:
      totalSum = 0
      for line in data:
         #.split() returns a list of strings... and removes whitespaces == \n as well
         rucksack = line.split() #array
         N = len(rucksack[0])
         first = rucksack[0][:(N//2)] #string
         sec = rucksack[0][(N//2):] #string
         firstSet = set(first)

         for c in sec:
            if c in firstSet:
               # we found our dup
               if c.isupper():
                  totalSum += (ord(c) - ord("A")) + 27
               else:
                  totalSum += (ord(c) - ord("a")) + 1
               break

      print(totalSum)

def partTwo():
   # every 3 lines is a group of all three elves
   # common between all 3 is the badge id
   # sum all the badge id of all the groups of 3s

   #find a list of all the badges
   with open("input.txt", "r") as data:
      badges = []
      group = []
     #read entire data doc, then split any empty whitespaces including "\n"
      for count, line in enumerate(data.read().split()):
         # print(count, list(line))
         group.append(line)
         if len(group) == 3:
            # every 3rd
            # find the badge; HAVE TO APPEAR IN ALL 3
            tmp1 = set(group[0])
            tmp2 = set(group[1])
            for c in group[2]:
               if c in tmp1 and c in tmp2:
                  badges.append(c)
                  break
            group = []
      
      #calculate the badge
      totalSum = 0
      for badge in badges:
         if badge.islower():
            totalSum += (ord(badge) - ord("a")) + 1
         else:
            totalSum += (ord(badge) - ord("A")) + 27
      print(totalSum)

partTwo()