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
   def __init__(self) -> None:
      self.cycle = 0 # count/timer
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

def main():
   with open("input.txt", "r") as data:
      instructions = [line.split() for line in data]
      signals = part1(instructions)
      part2(instructions)
      print(sum(signals))
      
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

def part2():
   # CRT horizontal pixels from i= 0 - 39
   #CRT draws a single pixel during each cycle
   # X determines where we are drawing?
   
if __name__ == "__main__":
   main()