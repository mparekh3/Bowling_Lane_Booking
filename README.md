# Bowling_Lane_Booking_System 

Fledged bowling lane booking system implemented in Python using EE-551-Fall-2019 knowledge.  

 

## Customers can 

 

* See available lanes. 

* Request for book lane. $15 will be charged for each lane per hour  

* Select number of players. $5 will be charged per player. 

* Return their booked-lane when a game is over. 

  

## Bowling_Lane_Booking_System Can  

 

* Display available lanes.  

* Take the request of customers for lanes. 

* Issue the bill to customers for their booked lane. 

* Update available lane list once a game is over. 

  

Here, by default we set five bowling lanes. So, five customers can book the lane in this system. Two classes are created in bowlinglane.py: Customer class and Bowlinglane class. 

### Customer Class: 

Customer lanes, their booking time and their bill are defined in this class so Each customer have their individual lanes, lane book time and bill for the game. 

 

### Bowlinglane Class: 

This class define the bowling lane system. This class include Lane display function, Take a number of player input function, Lane booking function, lane request function and game over function. 

##### Displaylane function: display avialable all lanes to customers. 

##### Players function: Take a number players value. 

##### Booklane function: This function initialized customers values line book lane line and number of players on those lanes. These values are used for billing when customer end the game. 

##### Reqestlane function: In this function, Customer allocated a lane from available lane    list and Available lane list is updates for the next customer. 

##### Gameover function: This function takes booked lane request from the customer when customer end the game. Bill is calculated in this lane and issue for customer. After taking the request of lane. Available lane list is also updated in this function. 

## How to run? 

This code is written in python3.6.
Open Terminal(for mac/linux) or command promp (windows) and clone this repository.
change directy to cloned repostiory by typing: 
###### cd Bowling_Lane_Booking

To run program type

###### python main.py


![bwlanebk1](https://user-images.githubusercontent.com/54687903/69931214-6dea2c00-1494-11ea-8360-e90dfa675183.png)


or depending upon your config 

###### python3 main.py 

![bwlanebk2](https://user-images.githubusercontent.com/54687903/69930466-945a9800-1491-11ea-9267-e68482e2ba0d.PNG)

You see screen like this:


![demo1](https://user-images.githubusercontent.com/54687903/69930535-ccfa7180-1491-11ea-9b36-b9df0737fcf2.PNG)


###### To see available lanes select option: 1. Display available lanes


![demo2](https://user-images.githubusercontent.com/54687903/69930570-ec919a00-1491-11ea-8420-a3e829dd0d81.PNG)


###### To book lane, select option: 2. Select lane
Here, System is located lane to customer and ask about number of players.

![demo3](https://user-images.githubusercontent.com/54687903/69930649-4e520400-1492-11ea-897d-4f7891ef9063.PNG)

for example: here we located lane: 5 and we select 2 players for this lane. We will charged $15 per hour for lane and $5 per player.

###### To finish the game, select option: 3. Game Over
here, System is asking about your allocated lane. Any lane game can be over any time. We do not have to follow the sequences. Customers can see the bill for their game.

![demo4](https://user-images.githubusercontent.com/54687903/69930786-c6b8c500-1492-11ea-839e-8d6a7e232e1c.PNG)

For example: here we want to over the game for lane 5.

###### We can close the application by selection option: 4. Eixt


![demo5](https://user-images.githubusercontent.com/54687903/69931147-2499dc80-1494-11ea-9913-0b973cf25a49.PNG)
