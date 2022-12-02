#Rock paper scissors
#first column is what your opponent is going to play A B C
# second column is what i should play X Y Z

#(1 for Rock, 2 for Paper, and 3 for Scissors)
#(0 if you lost, 3 if the round was a draw, and 6 if you won).

def partOne():
   with open("input.txt", "r") as data:
      # we need to save the scoring sheet
      # then line by line calculate the score
      janken = {"A":("Y","X") , "B":("Z","Y"), "C":("X","Z")} #opponent: (we win, draw)
      score = {"X":1,"Y":2,"Z":3}
      totalSum = 0
      for line in data.read().split("\n"):
         opponent = line[0]
         us = line[2]
         # if we win
         if janken[opponent][0] == us:
            totalSum += 6
         # draw
         elif janken[opponent][1] == us:
            totalSum += 3
         #lose dont add

         totalSum += score[us]
         

      print(totalSum)

def partTwo():
   # ROCK = A,X; PAPER = B,Y; SCISSOR = C,Z
   # X: LOSE, Y: DRAW, Z: WIN
   with open("input.txt", "r") as data:
      #opponent: (we,lose, draw, we win)
      janken = {"A":("Z","X","Y") , "B":("X","Y","Z"), "C":("Y","Z","X")} 
      score = {"X":1,"Y":2,"Z":3}
      totalSum = 0
      for line in data:
         # if X we lose
         if line[2] == "X":
            choice = janken[line[0]][0]
            totalSum += score[choice]
         # if Y we draw
         elif line[2] == "Y":
            choice = janken[line[0]][1]
            totalSum += score[choice] + 3
         # if Z we win
         elif line[2] == "Z":
            choice = janken[line[0]][2]
            totalSum += score[choice] + 6

      print(totalSum)
partTwo()