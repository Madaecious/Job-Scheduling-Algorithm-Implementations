###################################################################################################
# This generates jobs with random lengths and puts them in job.txt
# ------------------------------------------------------------------------
# Mark Barros
# CS 4310 - Operating Systems
# 2021 Summer Semester - California Polytechnic State University
###################################################################################################

# These is a necessary import for generating random integers.
import random

# These are modified versions of the programs and are for calculating and outputing
# only Average Turnaround Times.
import FCFS, SJF, RR2, RR5

# This is the count.
jobIteration = 1

# This is a constant specifying the number of jobs that will be generated.
NUMBER_OF_JOBS = 15

# This generates jobs of random burst rates and writes them in a file.
jobFile = open("job.txt", "w")
    
while jobIteration <= NUMBER_OF_JOBS:
    output = '{:>2}'.format(str(jobIteration))
    output = "Job " + output + "\n"
    jobFile.write(output)
    jobFile.write(str(random.randint(1, 25)) + "\n")
    jobIteration += 1

jobFile.close()

# This is the output for each algorithm.
print("-------------------------------------------------------")
print("Random Job Generator - By Mark Barros")
print("-------------------------------------------------------")
print("First Come First Served With " + str(NUMBER_OF_JOBS) + " Jobs:")
FCFS.fcfs()
print("\nShortest Job First With " + str(NUMBER_OF_JOBS) + " Jobs:")
SJF.sjf()
print("\nRound Robin Two With " + str(NUMBER_OF_JOBS) + " Jobs:")
RR2.rr2()
print("\nRound Robin Five With " + str(NUMBER_OF_JOBS) + " Jobs:")
RR5.rr5()
print("-------------------------------------------------------\n")

# End of Module. ##################################################################################