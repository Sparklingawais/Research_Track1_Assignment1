# Research_Track1_Assignment1
We start from the solution of the exercise 3
Put the main code after the definition of the functions. The makes the robot to:
1)	Find the closest silver marker
2)	Approaches towards the closest silver marker
3)	Grab the closest silver marker
4)	Move the marker at its 180° and release there and turn back the robot
5)	Start again from 1)
6)	If Golden markers are detected
7)	if golden token is on right Robot moves left
8)	if golden token is on left Robot moves right
9)	Start again from 1)
    
The method see() of the class Robot returns an object whose attribute info.marker_type may be MARKER_TOKEN_GOLD or MARKER_TOKEN_SILVER, depending of the type of marker (golden or silver). 
Modify the code of the exercise3 to make the robot:
1)	Retrieve the distance and the angle of the closest silver marker. If no silver marker is detected, the robot should rotate in order to find a marker.
2)	Drive the robot towards the marker and grab it
3)	Move the marker at its 180° (when done, you can use the method release() of the class Robot in order to release the marker)
4)	Retrieve the distance and the angle of the closest golden marker. If golden token is detected, the robot should move against it or if no golden is detected, the robot moves straight.
5)	start again from 1)
