################################################################################
# Author: Ming-Cee Yee
# Date Created: 2015-06-03
# Description: Changes system volume to given volume and opens given hyperlink
#     when the given time of day has been reached.
# References:
################################################################################

from datetime import datetime, time
from time import sleep

# returns input if lowerBound <= input < upperBound
def getIntegerInput(prompt, lowerBound, upperBound):
    valid = False
    while not valid:
        value = input(prompt)
        if lowerBound <= value and value < upperBound:
            valid = True
        print("Input should be greater than or equal to ", lowerBound, " and less than ", upperBound)
    return value

def main():
    # get time
    timeHour = getIntegerInput("Hour (24H time): ", 0, 24)
    timeMinute = getIntegerInput("Minute: ", 0, 60)
    #nextTime = time(timeHour, timeMinute)

    # get volume
    newVolume = getInput("Volume: ", 0, 101)

    # get hyperlink (no input guard!!)
    hyperlink = input("Hyperlink: ")

    # get current time
    currentTime = datetime.now().time()
    # calculate difference between now and the desired time
    # WILL BREAK IF DESIRED TIME DOES NOT OCCUR AFTER CURRENT TIME
    deltaHour = timeHour - currentTime.hour
    deltaMinute = timeMinute - currentTime.minute
    
    # sleep for time difference
    sleep((deltaHour*60*60)+(deltaMinute*60))
    
    # change system volume
    # open hyperlink

# run program
main()
