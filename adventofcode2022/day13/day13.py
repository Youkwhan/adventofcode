# distress signal => decoded out of order

# given a pair of packets, each pair seperated by a \n
# How many pairs of packets are in the right order?

#Packets:
   #  lists and integers

#Ordering rules:
#1) Both integers: left <= right 
#2) Both are lists: zip(left <= right) and len(left) < len(right)
from typing import List
from functools import cmp_to_key

class Packet:
   def __init__(self, pair1, pair2) -> None:
      self.pair1 = pair1 #list[int]
      self.pair2 = pair2
   
   # def compare_packet_pairs(self, pair1, pair2) -> bool:
   #    print(pair1, end=" / ") #str:"[1,2,3,]"
   #    print(pair2)
      
   #    # left and right
   #    for left, right in zip(pair1, pair2):
   #       print(left, right)
   #    # if they both values
   #       if isinstance(left, int) and isinstance(right, int):
   #          if left < right:
   #             return True
   #          elif right > left:
   #             return False
            
   #    # if they both lists
   #       elif isinstance(left, list) and isinstance(right, list):
   #          return self.compare_packet_pairs(left, right)

   #    # if one or the other
   #       else:
   #          if isinstance(left, list):
   #             return self.compare_packet_pairs(left,[right])
   #          else:
   #             return self.compare_packet_pairs([left],right)
   #    else:
   #       #runs out of elements
   #       if not pair1 and not pair2: #[],[] or [4,4], [4,4]
   #          return True
   #       if not pair1:
   #          return True
   #       if not pair2:
   #          return False
   
   def compare(self, p1, p2, lenl, lenr)->bool:
      while True:
         try: l, r = next(p1), next(p2)
         except StopIteration: # (4) if either l or r is empty
            if lenl == lenr: return None
            return True if lenl < lenr else False
         # (1) if both are int
         if isinstance(l, int) and isinstance(r, int):
            if l < r: return True
            if l > r: return False
         # (2) if both are list
         elif isinstance(l, list) and isinstance(r, list):
            res = self.compare(iter(l), iter(r), len(l), len(r))
            if res is not None:
               return res
         # (3) if one is list 
         elif (isinstance(l, list) and isinstance(r, int)) or (isinstance(l, int) and isinstance(r, list)):
            if isinstance(l, int): res = self.compare(iter([l]), iter(r), 1, len(r))
            else: res = self.compare(iter(l), iter([r]), len(l), 1)
            if res is not None:
               return res

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right: return -1
        if left > right: return +1
        return 0
    else:
        left = list([left]) if isinstance(left, int) else left
        right = list([right]) if isinstance(right, int) else right
        
        if len(left) == 0 and len(right) != 0: return -1 
        if len(right) == 0 and len(left) != 0: return +1
        if len(left) == 0 and len(right) == 0: return 0
        
        if (ret := compare(left[0], right[0])) != 0:
            return ret
        else:
            return compare(left[1:], right[1:])



def main() -> None:
   with open("input.txt", "r") as data:
      list_packets = [[eval(pair) for pair in pairs.split()] for pairs in data.read().split("\n\n")]
      right_order = part1(list_packets) #list of list of numbers
      print(part2(list_packets))

def part1(packets) -> List[int]:
   right_order_idx = []
   list_packets = [Packet(packet[0], packet[1]) for packet in packets]
   # now we have a list of Packet Objects which holds two pairs
   
   # we need to check if each Packet is in the right order
   for i, packetObj in enumerate(list_packets):
      # i tells us which packet we are checking (and which pair index to add if true)
      # if packetObj.compare_packet_pairs(packetObj.pair1, packetObj.pair2):
      #    right_order_idx.append(i+1)
      if packetObj.compare(iter(packetObj.pair1), iter(packetObj.pair2), len(packetObj.pair1), len(packetObj.pair2)):
         right_order_idx.append(i+1)

   return right_order_idx

def part2(packets):
   pack = []
   for packet in packets:
      pack.append(packet[0])
      pack.append(packet[1])
   pack.extend([[[2]], [[6]]]) # add new packet pair
   print(pack)
   pack.sort(key=cmp_to_key(compare))
   return (pack.index([[2]])+1) * (pack.index([[6]])+1)

if __name__ == "__main__":
   main()