#***********************************************************************
# Program:
#    Assignment 02
#    Brother Parrish, CS241
# Author:
#    Jandy Kiger
# Summary:  file reading
#**********************************************************************

import csv
import math

def filename_prompt():
    #Prompt the user for a filename.
    filename = input("Please enter the data file: ")
    return filename

def  find_rate(filename):
    '''Open the requested file and read through it line by line.
    Find the column for comm_rate and keep track of it as needed
    find min, max, and average.'''
    with open(filename) as rate_file: 
        reader = csv.DictReader(rate_file, delimiter = ',')
        commercial_rate = 0.0
        row_count = 0.0
        low_rate = 1.0
        high_rate = 0.0
        high = []
        low = []
        rate = 0.0
        avg = 0.0
        test = []
        for row in reader:
            #if row_count != 0:
            #columns = row.split(',')
            rate = float(row['comm_rate'])
            row_count += 1.0
            test.append(rate)
            if rate > high_rate:
                high_rate = rate
                high = row
            elif rate < low_rate:
                low_rate = rate
                low = row
            commercial_rate += rate
        avg = commercial_rate / row_count

    print ("\nThe average commercial rate is: {}".format (float(avg)))
    print ("\nThe highest rate is:\n{} ({}, {}) - ${}".format(high['utility_name'],high['zip'],high['state'],high['comm_rate']))
    print ("\nThe lowest rate is:\n{} ({}, {}) - ${:.1f}".format(low['utility_name'],low['zip'],low['state'],low_rate))

def main():
    #Runs through all the functions
    filename = filename_prompt()
    find_rate(filename)
if __name__ == "__main__":
    main()
