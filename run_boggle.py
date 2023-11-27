import string
import random



def roll(): #a function that returns a 2d list of 16 random letters from a to z
    i=0
    j=0
    row_collumn = [ [0]*4 for i in range(4)]
    for i in range(0,4):
        for j in range(0,4):
            row_collumn[i][j] = random.choice(string.ascii_lowercase)
    return row_collumn

def right_letters(): #rolls until there is the right amount of each letter, returns a 2d list of 16 random letters from a to z
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    correct = False
    while correct == False:
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

def rules():
    print("BOGGLE")
    print("Enter words made from letters on the board.")
    print("The words may not be less than three letters, use the same space twice, or connect to a letter outside of the surrounding blocks.")
    print("Every 'Q' on the board will be considered to be a 'Qu'.")
    print("Set a timer for two minutes and write down words made until the time runs out.")
    print("Both players will then type in their words and enter 'x' when finished.")
    print("A winner will be determined by how many unique words each player has.")
    print()


def right_spaces(word, board): #takes the word and checks to see if the letters are connected correctly, outputs a boolean (each letter follows from the last)
    for i in range(4):
        for j in range(4):
            if DFS(word, board, i, j):
                return True
    return False



def DFS(word, board, r, c):
    if board[r][c] != word[0]:  #if the coordinates i + j of the loop isn't equal to the first letter, exit and try the next combination
        return False
    if len(word) == 1:
        if board[r][c] == word[0]: #if the end of the word is reached and the combination i + j is correct, return true overall
            return True
        else:
            return False
    next_letter = word.replace(word[0], "", 1)
    if((r-1)>-1):
        if DFS(next_letter, board, r-1, c):
            return True
    if ((r+1)<4):
        if DFS(next_letter, board, r+1, c):
            return True
    if ((c-1)>-1):
        if DFS(next_letter, board, r, c-1):
            return True
    if ((c+1)<4):
        if DFS(next_letter, board, r, c+1):
            return True
    if ((r+1)<4) and ((c+1)<4):
        if DFS(next_letter, board, r+1, c+1):
            return True
    if ((r+1)<4) and ((c-1)>-1):
        if DFS(next_letter, board, r+1, c-1):
            return True
    if ((r-1)>-1) and ((c+1)<4):
        if DFS(next_letter, board, r-1, c+1):
            return True
    if ((r-1)>-1) and ((c-1)>-1):
        if DFS(next_letter, board, r-1, c-1):
            return True
    return False
    

def compare(one, two): #takes the lists of words found by each player, removes non-unique words and outputs the winner and the score
    same = []
    for word1 in one: #goes through both lists and removes duplicates
        remove = False
        for word2 in two:
            if word1 == word2:
                remove = True
        if remove == True:
            one.remove(word1)
            two.remove(word1)
            same.append(word1)
    if len(one) > len(two):
        print(f"Player one wins. Number of uniqe words was {len(one)}, while the number of player two's unique words was {len(two)}.")
    elif len(one) < len(two):
        print(f"Player two wins. Number of uniqe words was {len(two)}, while the number of player two's unique words was {len(one)}.")
    elif len(one) == len(two):
        print(f"Tie. Number of unique words for each is {len(one)}")
    else:
        print("Tie. No unique words.")
    print(f"Words removed: {same}")



rules()
b = right_letters()  #takes probable 2d list of a roll
make_board(b)  #prints a board with that roll
print()
user_word = "" #do I need to initialize?
p1_words = []
print("Player One")
while user_word != "x":
    user_word =  (input("Enter a word or x to finish: "))
    user_word = user_word.lower()
    length = len(user_word)
    if user_word == "x":
        print("Finished")
        print()
    elif (length < 3) and (right_spaces(user_word, b) == False):
        print("your word is too short and the letters are not connected correctly")
    elif (length < 3):
        print("your word is too short")
    elif right_spaces(user_word, b) == False:
        print("the letters are not connected correctly")
    elif p1_words.count(user_word)>0:
        print("already in the list")
    else:
        p1_words.append(user_word)
p2_words = []
print("Player Two")
user_word = ""
while user_word != "x":
    user_word =  (input("Enter a word or x to finish: ")).lower()
    if user_word == "x":
        print("Finished")
        print()
    elif (len(user_word) < 3) and (right_spaces(user_word, b) == False):
        print("your word is too short and the letters are not connected correctly")
    elif (len(user_word) < 3):
        print("your word is too short")
    elif right_spaces(user_word, b) == False:
        print("the letters are not connected correctly")
    elif p2_words.count(user_word) > 0:
        print("already in the list")
    else:
        p2_words.append(user_word)

compare(p1_words, p2_words)



#add a path to DFS
#add a library to say if the word's correct
#add a timer maybe
#look up actual rules
#maybe count longer words as more points?