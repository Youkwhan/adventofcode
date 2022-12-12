# darn monkeys playing with my missing items!
# we need to predict where the monkeys will throw.
# They opeerate based on how worried I am of each item

# MONKEY FUNCTION:
# starting items: is my worry level
# Operation: is how my worry level changes as the monkey inspects
# (BEFORE TEST): relief => int(worrylevel / 3) nearest integer
# Test: is how the monkey decides based on my worry level

# Rounds: Each monkey taks a single turn
# Signle turn: each monkey throws all their items one at a time before the next monkey continues

# Recieveing: 
# items goes to the end of the recipient list.
# if monkey has no items end turn.

# RETURN
# OVER 20 ROUNDS
# count the number of times each monkey inspects items
# FIND THE total monkey business = two most active monkeys count (multiplied)

# SOlution:
# class: Monkey(var:starting_items, var:inspection, func:operation, func:test)
# ds:

# we are going to parse by monkey and create a list of monkeys
# where the list = single round of monkyes

def main():
   with open("test.txt", "r") as data:
      monkeys = [line.split() for line in data]
      print("".join(monkeys)) #if we join then each monkey would be split by a single space
      
      

      monkeys = {} # monkey_id : Monkey

      

if __name__ == "__main__":
   main()