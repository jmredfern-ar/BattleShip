#from termcolor import colored
import random
import os

# CREATE BOARDS
ROWS = 10
COLS = 10
player1 = []
computer = []
ships =   ['C', 'B', 'R', 'S', 'D']
lengths = [ 5,   4,   3,   3,   2]
direction = ["RIGHT", "DOWN"]

# CLEAR THE CONSOLE
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# POPULATE BOARD
for i in range(ROWS): #LOOPS 10 TIMES
    row = [] 
    for j in range(COLS): #LOOPS 10 X 10 TIMES
        row.append('*')
    player1.append(row)
    computer.append(row)

# VALIDATE THAT IT IS POSSIBLE TO PLACE A SHIP
'''
def canPlaceShip(ship, length, direction, r, c):
    if computer[r][c] == "*":
        if
    else:
        return False
'''    

# COMPUTER PLACE SHIPS
def placeComputerShips():

    tryAgain = True
    while tryAgain:
        path = []
        index = 2 # DESTROYER
        d = random.choice(direction)
        if d == "RIGHT":
            r = random.randrange(0, ROWS)
            c = random.randrange(0, COLS - 1)
            if computer[r][c] == '*':
                path.append([r, c])
                index -= 1
                for i in range(index):
                    c += 1
                    if computer[r][c] == '*':
                        path.append([r, c])
                        tryAgain = False
                    else:
                        tryAgain = True
    print(path)
    for row in path:
        computer[row[0]][row[1]] = 'D'
        
        

# PLACE SHIP BY ENTERING EACH ROW/COL
def placeShipRC():
    running = True
    while running:

        if len(ships) == 0:
            running = False

        print("Choose a ship to place on your board")
        print(ships)
        ship = input(" >> ")
        if ship in ships:
            index = ships.index(ship)
            length = lengths[index]
            for i in range(length):
                r = int(input("Enter row >> "))
                c = int(input("Enter col >> "))
                player1[r][c] = ship
            ships.remove(ship)
            printBoard()
        else:
            print("Something went wrong!")

            

# PLACE SHIP BY ENTERING START AND END ROW / COL
def placeShipSE():
    running = True
    while True:

        if len(ships) == 0:
            running = False
        else:
            print("Choose a ship to place on your board")
            printShips()
            printLengths()
            ship = input(" >> ").upper()
            if ship in ships:

                    # GET LENGTH OF SHIP
                    LENGTH = lengths[ships.index(ship)]

                    # GET STARTING AND ENDING COORDS
                    startRow = int(input("Enter starting row >> "))
                    startCol = int(input("Enter starting col >> "))
                    endRow = int(input("Enter ending row >> "))
                    endCol = int(input("Enter ending col >> "))
                            
                    # CHECK TO MAKE SURE ENTRIES ARE INSIDE GRID - TODO MAKE FUNC
                    if startRow < 0 or startRow >= ROWS:
                        print("INVALID: Start Row out of range.")
                    elif endRow < 0 or endRow >= ROWS:
                        print("INVALID: End Row out of range.")
                    elif startCol < 0 or startCol >= COLS:
                        print("INVALID: Start Row out of range.")
                    elif endCol < 0 or endCol >= COLS:
                        print("INVALID: End Row out of range.")

                    # VER OR HOR?
                    elif startRow == endRow: # HORIZONTAL
                        if endCol - startCol > LENGTH:
                            print("INVALID: Ship size incorrect, s/b ", LENGTH)
                        else:
                            col = startCol
                            
                            for i in range(LENGTH - 1):
                                col += 1
                                player1[startRow][col] = ship
                                
                            player1[startRow][startCol] = ship
                            player1[endRow][endCol] = ship

                            # REMOVE SHIP AND LENGTH FROM LISTS
                            del lengths[ships.index(ship)]
                            ships.remove(ship)
            printBoard()
            
# PRINT BOARD
def printPlayerBoard():
    r = 0
    print("  0 1 2 3 4 5 6 7 8 9 ")
    for row in player1:
        print(r, end = " ")
        r += 1
        for elem in row:
            print(elem, end = " ")
        print()

def printComputerBoard():
    r = 0
    print("  0 1 2 3 4 5 6 7 8 9 ")
    for row in computer:
        print(r, end = " ")
        r += 1
        for elem in row:
            print(elem, end = " ")
        print()

# PRINT SHIP LIST
def printShips():
    for elem in ships:
        print(elem, end = " ")
    print()

# PRINT LENGTH LIST
def printLengths():
    for elem in lengths:
        print(elem, end = " ")
    print()

# MAIN GAME LOOP
print("B A T T L E S H I P !")
#printPlayerBoard()
print()
#printComputerBoard()
placeComputerShips()
printComputerBoard()

# PLACE SHIPS
#placeShipRC()
#placeShipSE()

