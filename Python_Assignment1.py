from __future__ import print_function
import time
from sr.robot import *

'Defined Threshold Values'
silver_th = 0.5 # Defined threshold value to find the Silver Box's Linearly
golden_th = 0.75 # Defined threshold value to find the Golden Box's Linearly, if the value is smaller it increases the risk of crashing against the wall, and if its value is greater then robot will not be stably aligned
angle_th = 10.0 # Defined threshold value to control the orientation

'Calling of class Robot'
R = Robot()

'Function to find the Golden Token'
def FindGoldenToken():
	golden_area=100
	for token in R.see():
		if token.dist < golden_area and token.info.marker_type is MARKER_TOKEN_GOLD:
		   golden_area = token.dist
		   golden_angle = token.rot_y
	if golden_area == 100:
		return -1, -1
	else:
		return golden_area, golden_angle# Returns nearest golden linear distance value and angular distance value, if no golden detected it will retuen -1,-1

'Function for setting an angular vilocity'
def turn(speed, seconds):
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0


'Function to find the Silver Token'
def FindSilverToken():
	silver_area=100
	for token in R.see():
		if token.dist < silver_area and token.info.marker_type is MARKER_TOKEN_SILVER and -120 <token.rot_y < 120:
		   silver_area=token.dist
		   silver_angle=token.rot_y
	if silver_area == 100:
		return -1, -1
	else:
		return silver_area, silver_angle # Returns nearest silver linear distance value and angular distance value, if no silver detected it will retuen -1,-1
   	
'Function for setting a linear vilocity'
def drive(speed, seconds):
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

    
while 1:
    silver_area, silver_angle=FindSilverToken() # calling of function to find Silver token if nearby and storing there result values in some variables
    golden_area, golden_angle=FindGoldenToken() # calling of function to find Golden token if nearby and storing there result values in some variables
   
    if silver_area==-1: 
     	print("Sorry there is no Silver Token nearby in a range.")
		exit()  # if silver markers is not detected, the program ends
    
    'Capturing of Silver Token'
    elif silver_area < silver_th: # If the Token is detected, Robot will grab the box, it will turn in clockwise direction, leaves the box, goes backword a bit, turning counter-clockwise direction, and then moves forward.
		print("I'm Coming for you noughty box (:")
		R.grab() # Grabing the nearest Silver Token
		print("I got you little one ;)")
		turn(+15, 4.0) # calling a funtion followed by values to turn the robot at some directon angularly
		R.release() # Releasing the grabbed token
		turn(+0, 2.0)
		drive(-10, 2.0) # calling a funtion followed by values to turn the robot at some directon linearly
		turn(-15, 4.0)
		drive(15, 2.5)

	'Alignment of the Robot compaired to wall'
    elif golden_area < golden_th:
    	print("Watch out! there is a wall ahead :(")
		if golden_angle > 0: # In this case, wall is detected on the right side of the robot, so it will turn a bit left
	   		print("A bit Left")
	   		drive(-7.5, 1)	   
	   		turn(-5, 1.0)
	   		drive(10, 2)
		else: # In this case, wall is detected on the left side of the robot, so it will turn a bit right
	   		print("A bit Right")
	   		drive(-7.5, 1)
	   		turn(+5, 1.0)
	   		drive(10,2)

   	'Aproaching the detected Silver Box'
	elif -angle_th <= silver_angle <= angle_th: 
        print("There you are nouthy silver, I'm coming straight for you...;)")
        drive(20, 0.5)#going straight towards the box
    
'Alignment od Robot compaired to Silver Token'
    # If the robot is not well aligned with the token, we move it towards left or right depending on the angular distance
    elif silver_angle < -angle_th: 
        print("A bit Left.///")
        turn(-10, 0.1)
        drive(10, 0.4)
    
    elif silver_angle > angle_th:
        print("A bit Right.///")
        turn(+10, 0.1)
        drive(10, 0.4)