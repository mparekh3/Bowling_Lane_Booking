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

###### Displaylane function: display avialable all lanes to customers. 

###### Players function: Take a number players value. 

###### Booklane function: This function initialized customers values line book lane line and number of players on those lanes. These values are used for billing when customer end the game. 

###### Reqestlane function: In this function, Customer allocated a lane from available lane    list and Available lane list is updates for the next customer. 

###### Gameover function: This function takes booked lane request from the customer when customer end the game. Bill is calculated in this lane and issue for customer. After taking the request of lane. Available lane list is also updated in this function. 

## How to run? 

This code is written in python3.6 

Simply run 

python main.py 

or depending upon your config 

Python3 main.py 
