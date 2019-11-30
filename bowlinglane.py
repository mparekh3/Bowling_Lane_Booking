import datetime

class Customer:
    """
    This class is define custormers` values like Lane, Booking Time and Bill.
    """
    def __init__(self):

        self.lane = 0
        self.bookTime = 0
        self.bill = 0

class Bowlinglane:
    """
    This Class defines functions of the bowling lane system.
    Includes:
        +Displaying Lanes.
        +Booked Lanes.
        +Return Bills when game is over.
    """
    def __init__(self,avaialble = 0):
        lane_count = avaialble
        self.available = list(range(1,lane_count+1))
        ##Booked Time for each lane.
        self.lane1_time = datetime.datetime.now()
        self.lane2_time = datetime.datetime.now()
        self.lane3_time = datetime.datetime.now()
        self.lane4_time = datetime.datetime.now()
        self.lane5_time = datetime.datetime.now()
        ##Number of Players in each lane.
        self.player_lane1 = 0
        self.player_lane2 = 0
        self.player_lane3 = 0
        self.player_lane4 = 0
        self.player_lane5 = 0

    def displaylane(self):
            """
            Displays the Lane currently available for booking.
            """
            print("We have currently {} lanes available.".format(self.available))
            return self.available

    def players(self):

        player = input("How many players are playing?:")

        try:
            player = int(player)
            return player

        except ValueError:
            print("That`s not a positive integer!")
            return -1

        print("""You will charge $5 per player. Enjoy your game.""")

    def Booklane(self,n):

        if n == -1:
            print("This lane has not been booked.")
        else:
            customer = Customer()
            customer.lane = n
            if n == 1:
                self.lane1_time = datetime.datetime.now()
                self.player_lane1 = self.players()
            elif n == 2:
                self.lane2_time = datetime.datetime.now()
                self.player_lane2 = self.players()
            elif n == 3:
                self.lane3_time = datetime.datetime.now()
                self.player_lane3 = self.players()
            elif n == 4:
                self.lane4_time = datetime.datetime.now()
                self.player_lane4 = self.players()
            else:
                self.lane5_time = datetime.datetime.now()
                self.player_lane5 = self.players()



    def requestlane(self):

        if self.available != None:
            print("Lane:{} is booked for you. You will be charged $15 per hour for this lane.".format(self.available[-1]))
            return self.available.pop()
        else:
            return -1

    def gameover(self):

        custo_lane = input("Which lane you had?")
        numOfperson = 0

        try:
            custo_lane = int(custo_lane)
        except ValueError:
            print("That`s not a positive integer!")
            return -1
        if not custo_lane in self.available:

            if custo_lane == 1:
                start_time = self.lane1_time
                numOfperson = self.player_lane1
            elif custo_lane == 2:
                start_time = self.lane2_time
                numOfperson = self.player_lane2
            elif custo_lane == 3:
                start_time = self.lane3_time
                numOfperson = self.player_lane3
            elif custo_lane == 4:
                start_time = self.lane4_time
                numOfperson = self.player_lane4
            else:
                start_time = self.lane5_time
                numOfperson = self.player_lane5

            self.available.append(custo_lane)
            end_time = datetime.datetime.now()
            gameTime = end_time - start_time

            bill = round(gameTime.seconds/3600)*15+(numOfperson*5)

            print("Thank for coming. Hope you enjoyed the game!")
            print("That would be ${}".format(bill))

            return bill

        else:
            print("Sorry, This lane is not booked yet")
            return -1
