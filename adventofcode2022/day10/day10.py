# set of instructions, that can either be:
#  - noop: wait one cycle
#  - addx V : wait twwo cycles and add V to x on the third cycle

# we check signal strength at 20, and every 40
# signal strength = x * cycle#

# we need to independelty track cycles
# and a count of x
# (count: x)
from typing import List

class Clock():
   def __init__(self, cycle=0) -> None:
      self.cycle = cycle # count/timer
      self.x = 1
      self.signals = []
   
   def noop(self) -> None:
      self.cycle += 1
      self.check_signal()

   def addx(self, val) -> None:
      for _ in range(2):
         self.cycle += 1
         self.check_signal()
      self.x += val
   
   def check_signal(self) -> None:
      # CHECK at cycle 20 and every other 40
      if self.cycle == 20 or (self.cycle - 20) % 40 == 0:
         self.signals.append(self.x * self.cycle)

   def execute_noop(self, screen) -> None:
      self.cycle += 1
      self.check_sprite(screen)

   def execute_addx(self, val, screen)->None:
      for _ in range(2):
         self.cycle+= 1
         self.check_sprite(screen)
      self.x += val
   
   def check_sprite(self, screen):
      if self.cycle%40 in [self.x-1, self.x, self.x+1]:
         screen[self.cycle//40][self.cycle%40] = "#"
      else:
         screen[self.cycle//40][self.cycle%40]= " "



def main():
   with open("input.txt", "r") as data:
      instructions = [line.split() for line in data]
      signals = part1(instructions)
      # print(sum(signals))
      screen = [[" " for _ in range(40)] for _ in range(6)]
      part2(instructions, screen)
      visual(screen)

def visual(screen):
   for line in screen:
      print("".join(line))
      
     
def part1(instructions) -> List[int]:
   device = Clock()
   for signal in instructions:
      cmd = signal[0]
      if cmd == "noop":
         device.noop()
      elif cmd == "addx":
         device.addx(int(signal[1]))
   # print(device.cycle)
   # print(device.x)
   # print(device.signals)
   return device.signals

def part2(instructions, screen) -> List[List[str]]:
   # CRT horizontal pixels from i= 0 - 39
   #CRT draws a single pixel during each cycle
   # X is represented by 3 spaces.
   # If our cycle index overlaps with our X index we draw at the cycle index, otherwise dark(.)
   device = Clock(cycle=-1) # x = 1
   for signal in instructions:
      cmd = signal[0]
      if cmd == "noop":
         device.execute_noop(screen) #cycle index, x index
      elif cmd == "addx":
         device.execute_addx(int(signal[1]), screen)
   
   #BREAKING NEWWS:
   # X ranges from 0-40 
   # so i need to recent every time cycle goes to a new line

   




   
if __name__ == "__main__":
   main()