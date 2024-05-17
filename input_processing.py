# input_processing.py
# Pahul Brar, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.

import sys


# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"

    # Replace these comments with your function commenting
    def update_status(self, light = None, pedestrian = None, vehicle = None): # You may decide how to implement the arguments for this function
        if light is not None:
            self.light = light
        elif pedestrian is not None:
            self.pedestrian = pedestrian
        elif vehicle is not None:
            self.vehicle = vehicle
        else:
            pass



# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    if(sensor.light == 'red' or sensor.pedestrian == "yes" or sensor.vehicle == "yes"):
        print('')
        print("STOP")
        print('')
    elif(sensor.light == 'green' and (sensor.pedestrian == "no" or sensor.vehicle == "no")):
        print('')
        print("Proceed")
        print('')
    elif(sensor.light == 'yellow' and (sensor.pedestrian == "no" or sensor.vehicle == "no")):
        print('')
        print("Caution")
        print('')
    print("Light = " + sensor.light + ", Pedestarian = " + sensor.pedestrian + ", Vehicle = " + sensor.vehicle)
    pass



# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    
while(True):
    mySensor = Sensor()
    while(True):
        print("Are Changes Detected in the Vision Input")
        try:
            selection = int(input("Select 1 for light, 2 for pedestarian, 3 for vehicle,or 0 to end the program: "))
            if(selection not in [0,1,2,3]):
                raise ValueError("You did not select a valid entry, please try again")
        except ValueError as e:
            print(e)
            continue
        if (selection == 0):
            print("Exiting Program")
            sys.exit()
        break
    while(True):
        try:
            change = input("What change has been identified?: ")
            if(((selection == 2 or selection == 3) and (change not in ['yes', 'no']) )or (selection == 1 and change not in ['red', 'yellow', 'green'])):
                raise ValueError("you did not provide a valid change please try again")
        except ValueError as e:
            print(e)
            continue
        if(selection == 1):
            mySensor.update_status(light = change)
            break
        elif(selection == 2):
            mySensor.update_status(pedestrian = change)
            break
        elif(selection == 3):
            mySensor.update_status(vehicle = change)
            break

    print_message(mySensor)


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

