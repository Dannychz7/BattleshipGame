import numpy
import random

class Game:
    def __init__(self):
        self.width = 10
        self.length = 10
    
    def printGameIntro(self):
        battleShip_text = """
            B B B      A    TTTTT  TTTTT L     EEEEE  SSSSS  H   H III  PPPP
            B   B     A A     T      T   L     E      S      H   H  I   P   P
            BBBBB    AAAAA    T      T   L     EEEE    SSSS  HHHHH  I   PPPP
            B   B   A     A   T      T   L     E          S  H   H  I   P
            B B B  A       A  T      T   LLLLL EEEEE  SSSSS  H   H III  P
            """
        Battleship_logo = """ 
                   ~;                           ;~   
                  ,/|\.                      ./|\.
                ,/' |\ \.                  ./ /| `\.
              ,/'   | |  \                 /  | |   `\.
            ,/'     | |   |               |   | |     `\.
          ,/'       |/    |               |    \|       `\.
        ,/__________|-----' ,           .  `----|__________\.
       ___.....-----''-----/             \-----''----.....___
       \                  /               \               ""/
    ~~-~^~^~`~^~`~^^~^~-^~^~^~-~^~^~^~~^~^~^~^~^`~^~^`^~^~^`^~^~^~^~
     ~-^~^-`~^~-^~^`^~^-^~^`^~^-~^~^~~^~~^~^~`~~^~^`~^~^~`~~^~^~~^~
        """
        msg = """ Welcome to Battleship, a Game where 6 boats are randomly placed in a 10 x 10 grid.
        Each boat is 3 to 4 places large and it is your job to find and shoot down each
        boat. You will have 50 bullets, so don't waste them. Thanks for playing !!! """
        print(battleShip_text)
        print(Battleship_logo)
        print(msg)
        print(" ")
    
    def createBoat(self):
        rand_num = random.randint(1, 98)
        rand_num2 = random.randint(1, 80) 
        if(random.randint(0,1) == 0):
            boat = [rand_num, rand_num + 1, rand_num + 2]
            #print(boat)
            return boat
        else:
            boat = [rand_num2, rand_num2 + 10, rand_num2 + 20]
            #print(boat)
            return boat
    
    def keepPlaying(self):
        while(True):
            playing = input("Would you like to keep playing? Yes or No? ").lower()
            if ((playing == "yes") or (playing == "y")):
               return True
            elif playing == "no" or playing == "n":
                return False
            else:
                print("Please enter yes or no.")
            
        
        
    def userAttack(self): 
      while True:
        try:
            numX = int(input("Enter the x coordinate for where you want to attack: "))
            numY = int(input("Enter the y coordinate for where you want to attack: "))
            return 10 * numY + numX + 1
        except ValueError:
            print("Please enter valid integers.")
        
        
    def revealShips(self, miss, hit, locations, boat):
        print("     0  1  2  3  4  5  6  7  8  9 ")
        for x in range(10):
            row = ""
            for y in range(10):
                index = x * 10 + y + 1
                if(index in miss):
                    ch = " O "
                elif(index in hit):
                    ch = " U "
                elif(index in boat) and (locations[index] == 0):
                    ch = " X "
                else:
                    ch = " _ "
                row = row + ch
            print(x, " ", row) 
    
    def sunkShip(self, hit, boat): # WORK IN PROGESS
        print(boat)
        new_boat = []
        hit_keys = []
        for hit_key in hit:
            hit_keys.append(hit_key)
            print("This is hit Keys ", hit_keys)
            for key in boat:
                new_boat.append(key)
            
                print("This is boat Keys ", new_boat)
                if(all(key in new_boat for key in hit_keys) and len(new_boat) == 3):
                    return True
                else: 
                    if len(new_boat) % 3 == 0:
                        print("Set: ", new_boat)
                        new_boat = []
        return False

    def sunkShip2(self, hit, boat): # WORK IN PROGRESS
        print(boat)
        new_boat = []
        hit_keys = []
        for hit_key in hit:
            hit_keys.append(hit_key)
            print("This is hit Keys ", hit_keys)
            for key in boat:
                new_boat.append(key)
                print("This is boat Keys ", new_boat)
                
                if all(key in new_boat for key in hit_keys) and len(hit_keys) >= 3:
                    print("Set: ", new_boat)
                    return True
        new_boat = []
        return False
                
        
    def createGameBoard(self):
        place = 0
        location = {} 
        print("     0  1  2  3  4  5  6  7  8  9 ")
        for x in range(10):
            row = ""
            for y in range(10):
                ch = " _ "
                row = row + ch
                place = place + 1
                
                #Creates 5 boats and returns their three coordinate locations
                location[place] = 1
                
            print(x, " ", row)  
        
        self.updateGameBoard(location)         
        
    def updateGameBoard(self, location):
        misses = {}
        hits = {}
        boats = {}
        for i in range(5):
            boat = self.createBoat()
            if(boat[0] in location):
                for i in range(3):
                    location[boat[i]] = 0
            for i in boat:
                boats[i] = " X "
        
        chances = 0
        while(chances <= 50 and self.keepPlaying()):
            count = self.userAttack()
            print("     0  1  2  3  4  5  6  7  8  9 ")
            for x in range(10):
                row = ""
                for y in range(10):
                    index = x * 10 + y + 1
                    if(index in misses):
                        ch = misses[index]
                        row = row + ch
                    elif(index in hits):
                        ch = hits[index]
                        row = row + ch
                    else:
                        ch = " _ "
                        if (index == count) and (location[index] == 0):
                            ch = " X "
                            hits[index] = " X "
                        elif (index == count) and (location[index] != 0):
                            ch = " O "
                            misses[index] = " O "
                        row = row + ch
                print(x, " ", row) 
            chances += 1
            # if(self.sunkShip2(hits, boats)):
            #     print("You sunk the USS Charlie! ")
            # else:
            #     continue
        print("Thanks for Playing! Here are the locations of the ships")
        self.revealShips(misses, hits, location, boats)
        
            

Game = Game()
Game.printGameIntro()
Game.createGameBoard() 
