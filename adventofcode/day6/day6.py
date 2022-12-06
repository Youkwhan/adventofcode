#find the first Marker
# The start of a packet marker == four characters that are all different
from collections import defaultdict
def partOne():
   with open("input.txt", "r") as data:
      data = data.read()
      window = defaultdict(int)
      numDistinct = 0
      left = 0
      for right in range(len(data)): 
         if data[right] not in window:
            numDistinct += 1   
         window[data[right]] += 1
         if (right-left+1) > 14: # condition change
            window[data[left]] -= 1
            if window[data[left]] == 0:
               del window[data[left]]
               numDistinct -= 1
            left += 1
         if numDistinct == 14: #change
            print(right+1)
            break
         
partOne()

#partTwo change the 4 into a 14