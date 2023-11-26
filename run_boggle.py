import string
import random



#if row_collumn[i[j]] == "q":
#                row_collumn[i[j]] = "qu"



#def right_letters(): honestly come back to this  #rolls until there is a probable amount of each letter and returns a 2d list of 16 random letters from a to z

 #   b = roll()
  #  correct = False
   # while correct == False:
    #    if (b.count("q")>1) or (b.count("x")>1) or (b.count("z")>1) or (b.count("j")>1):
     #       b = roll()
      #  elif (b.count("f")>2) or (b.count("k")>2) or (b.count("w")>2) or (b.count("v")>2):
       #     b = roll()
       # elif (b.count("b")>3) or (b.count("c")>3) or (b.count("g")>3) or (b.count("h")>3) or (b.count("p")>3) or (b.count("u")>3) or (b.count("y")>3):
       #     b = roll()
       # elif (b.count("d")>4) or (b.count("m")>4) or (b.count("r")>4):
       #     b = roll()
       # elif (b.count("l")>5) or (b.count("s")>5) or (b.count("n")>5):
       #     b = roll()
       # elif (b.count("t")>6) or (b.count("o")>6):
       #     b = roll() # 
       # elif (b.count("i")>7) or (b.count("a")>9) or (b.count("e")>10):
       #     b = roll()
       # else:
       #     correct = True




def roll(): #a function that returns a 2d list of 16 random letters from a to z
    i=0
    j=0
    row_collumn = [ [0]*4 for i in range(4)]
    for i in range(0,4):
        for j in range(0,4):
            row_collumn[i][j] = random.choice(string.ascii_lowercase)
    return row_collumn

def right_letters():
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    correct = False
    while correct == False:   #rolls until there is the right amount of each letter
        r = roll()
        a_count = []
        for letter in alphabet: #takes each letter of the alphabet in turn and counts how many there are in r
            letter_count = 0
            for i in range(4):
                for j in range(4):
                    if r[i][j] == letter:
                        letter_count += 1
            a_count.append(letter_count)
        if (a_count[16]>1) or (a_count[23]>1) or (a_count[25]>1) or (a_count[9]>1): #check whether the number of each letter exceeds what is possible, ordered in a way that makes sense
            correct = False
        elif (a_count[5]>2) or (a_count[10]>2) or (a_count[22]>2) or (a_count[21]>2):
            correct = False
        elif (a_count[1]>3) or (a_count[2]>3) or (a_count[6]>3) or (a_count[7]>3) or (a_count[15]>3) or (a_count[20]>3) or (a_count[24]>3):
            correct = False
        elif (a_count[3]>4) or (a_count[12]>4) or (a_count[17]>4):
            correct = False
        elif (a_count[11]>5) or (a_count[18]>5) or (a_count[13]>5):
            correct = False
        elif (a_count[19]>6) or (a_count[14]>6):
            correct = False
        elif (a_count[8]>7) or (a_count[0]>9) or (a_count[4]>10):
            correct = False
        else:
            correct = True
    return r

def make_board(roll):  #takes letters from a 2d list called roll and prints the board
    print("-"*17)
    for i in range(4):
        for j in range(4):
            x = (roll[i][j]).upper()
            print(f"| {x} ", end = "")
        print("|")
        print("-"*17)




b = right_letters()  #takes probable 2d list of a roll
make_board(b)  #prints a board with that roll



print()
print()  
print(b)
print(b[1][1])
b[1][1] = 'z'
print(b)



