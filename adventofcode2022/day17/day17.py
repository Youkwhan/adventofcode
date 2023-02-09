# where will the rocks fall next?
# five types of rocks, "#" = rock, "." = empty space
# they fall in this order:
# - shape, + shape, reverse L shape, | shape, [] shape

# rocks do not spin, but move left ro right by jet streams
# ONCE WE GET TO THE END OF THE LIST REPEAT: for jet pattern and falling rock pattern

# chamber: 7 wide
# rock appears 2 units from left wwall, 3 units above floor/rock
# jet push 1, fall down 1

# stopping condition: if a move causes it to stop

class Cave:
   def __init__(self, jet_pattern) -> None:
      pass


def part1(jet_pattern, rocks=2022):
   # make the cave
   cave = Cave(jet_pattern)
   
   #make several steps
   while cave.rock_counter < rocks:
      cave.step()
   print(f"The solution 1 is: {cave.highest+1}")

def parse_data(data: str)->list:
   return list(data.strip())

if __name__ == "__main__":
   with open("test.txt", "r") as data:
      data = data.read()
      jet_pattern = parse_data(data)
      part1(jet_pattern)