# every section has a unique ID number
# each elf is assigned a range of section IDs

# problem is overlaps
# so elves pair up to make a big list

def partOne():
   # find the number of pairs where one range fully contains the other.
   with open("input.txt", "r") as data:
      contain = 0
      for line in data.read().split():
         pairs = line.split(",")
         first, sec = pairs[0].split("-"),pairs[1].split("-")
         # print(first, sec)
         # if first pair contains the second?
         if int(first[0]) <= int(sec[0]) and int(first[1]) >= int(sec[1]):
            contain += 1
         elif int(first[0]) >= int(sec[0]) and int(first[1]) <= int(sec[1]):
            contain += 1
      print(contain)

def partTwo():
   # return number of pairs with any overlaps
    with open("input.txt", "r") as data:
      contain = 0
      for line in data.read().split():
         pairs = line.split(",")
         first, sec = pairs[0].split("-"),pairs[1].split("-")
         #overlaps if the first[end] >= sec[start]
         if int(first[1]) >= int(sec[0]) and int(first[0]) <= int(sec[1]):
            contain += 1
      print(contain)
partTwo()