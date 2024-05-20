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
# A class to represent the sensor status of the car's vision system.
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    # Initializes the Sensor object with default values.
    def __init__(self):
        self.light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"

    # The update function is passed the update values, and they are by default set to None, so they won't update unless user provides an update.
    # if something is update, then the value is changed for the object.
    def update_status(self, light = None, pedestrian = None, vehicle = None): # You may decide how to implement the arguments for this function
        if light is not None:
            self.light = light
        if pedestrian is not None:
            self.pedestrian = pedestrian
        if vehicle is not None:
            self.vehicle = vehicle


# The sensor object should be passed to this function to print the action message and current status
# Given the sensor object, based on the preset conditions, on the value of the sensor, a corresponding message is printed.
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
    print('')
    pass

# Main function to run the car vision detector processing program.
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    
    mySensor = Sensor()
    while(True):
        while(True):
            print("Are Changes Detected in the Vision Input")
            try:
                selection = int(input("Select 1 for light, 2 for pedestarian, 3 for vehicle,or 0 to end the program: "))
                if(selection not in [0,1,2,3]):
                    raise ValueError("You did not select a valid entry, please try again")
            except ValueError as e:
                print(e)
                print(' ')
                continue
            if (selection == 0):
                print("Exiting Program")
                sys.exit()
            break
        while(True):
            try:
                change = input("What change has been identified?: ")
                if(((selection == 2 or selection == 3) and (change not in ['yes', 'no']) )or (selection == 1 and change not in ['red', 'yellow', 'green'])):
                    raise ValueError("you did not provide a valid change, please try again")
            except ValueError as e:
                print(e)
                print(' ')
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

