#######################################################################################################
# Round-Robin with Time Slice = 2 Algorithm Implementation
# ------------------------------------------------------------------------
# By Mark Barros
# CS 4310 - Operating Systems
# 2021 Summer Semester - California Polytechnic State University
#######################################################################################################

# These are data structures. ##########################################################################

# This defines the job object. ------------------------------------------------------------------------
class Job:

    # These are the object's data attributes.
    jobNumber = "Job 0" # (equals the value given in job.txt)
    initialBurstTime = 0 # (equals the original value in the job.txt)
    remainingBurstTime = 0 # (decreases as it is incrementally sliced by the time quantum)
    finalSlice = False # (True if the job is near its end; otherwise it's False)

    # These are the object's methods.
    def setJobNumber(self, jobNumber):
        self.jobNumber = jobNumber

    def setInitialBurstTime(self, burstTime):
        self.initialBurstTime = self.remainingBurstTime = burstTime

    def calculateRemainingBurstTime(self):
        remaining = self.remainingBurstTime - SLICE
        if remaining > 0:
            self.remainingBurstTime -= SLICE
        else:
            self.finalSlice = True

# This defines the job slice object. ------------------------------------------------------------------
class JobSlice:

    # These are the object's data attributes.
    jobNumber = "Job 0" # (equals the value in the job object)
    initialBurstTime = 0 # (equals the original value in the job.txt)
    remainingBurstTime = 0 # (decreases as it is incrementally sliced by the time quantum)
    startTime = 0 # (equals either 0 or the end time of the previous job slice)
    endTime = 1 # (equals the start time plus the time quantum)
    completionTime = 0 # (equals the end time if and when the burst time is less than
                       #  or equal to zero)

    # These are the object's methods.
    def setJobNumber(self, jobNumber):
        self.jobNumber = jobNumber

    def setInitialBurstTime(self, initialBurstTime):
        self.initialBurstTime = self.remainingBurstTime = initialBurstTime

    def setRemainingBurstTime(self, remainingBurstTime):
        self.remainingBurstTime = remainingBurstTime

    def setStartTime(self, start):
        self.startTime = start

    def calculateEndTime(self, timeAmount):
        self.endTime = self.startTime + timeAmount

    def setCompletionTime(self):
        self.completionTime = self.endTime
    
# This defines a ready queue using a list object. -----------------------------------------------------
jobQueue = []

# This defines a job slice queue using a list object. -------------------------------------------------
jobSliceQueue = []

# This is a constant. ---------------------------------------------------------------------------------
SLICE = 2 # This is the Round-Robin time quantum.

# These are variables. ################################################################################

averageTurnaroundTime = 0 # This equals the sum of the completion times divided by the number of jobs.
numberOfJobs = 0 # This will be set to the number of jobs in the job object ready queue.
jobIndex = 0 # This index is used for the job object ready queue.
jobSliceIndex = 0 # This index is used for the job slice queue. 

# These are functions. ################################################################################

# This calculates the average turnaround time. --------------------------------------------------------
def calculateAverageTurnaroundTime():
    sumOfCompletionTimes = 0
    for w in range(len(jobSliceQueue)):
        sumOfCompletionTimes += jobSliceQueue[w].completionTime
    return "{:.2f}".format(sumOfCompletionTimes / numberOfJobs)

# This outputs the header. ----------------------------------------------------------------------------
def outputHeader():
    print()
    print("#########################################################################################")
    print()
    print("Round-Robin with Time Slice = 2 Algorithm Implementation - By Mark Barros")
    print()

# This outputs the schedule table to the monitor. -----------------------------------------------------
def outputScheduleTable():

    print("-----------------------------------------------------------------------------------------")
    print("| Job  # | Burst Time | Start Time | End Time | Remaining Time |     Completion Time    |")
    print("-----------------------------------------------------------------------------------------")

    for v in range(len(jobSliceQueue)):

        # This format's the job slice's job number for output.
        a = '{:>2}'.format(jobSliceQueue[v].jobNumber)

        # This specifies that a job's burst time is to be output only if the job slice
        # is the job's last, and format's the job's burst time for output.
        b = "      "
        if jobSliceQueue[v].completionTime != 0:
            b = '{:>6}'.format(jobSliceQueue[v].initialBurstTime)

        # This format's the job slice's start time for output.
        c = '{:>6}'.format(jobSliceQueue[v].startTime)

        # this format's the job slice's end time for output.
        d = '{:>5}'.format(jobSliceQueue[v].endTime)

        # This specifies that a job slice's remaining burst time is to be output as a zero if the
        # remaining burst time is less than zero and otherwise outputs the remaining burst time.
        # It also formats the output of both.
        if jobSliceQueue[v].remainingBurstTime < 0:
            e = '{:>8}'.format(0)
        else:
            e = '{:>8}'.format(jobSliceQueue[v].remainingBurstTime)

        # This specifies that a job's completion time is to be output only if the job slice
        # is the job's last, and formats the job's completion time for output.
        f = "                      "
        if jobSliceQueue[v].completionTime != 0:
            f = jobSliceQueue[v].jobNumber + " completed @" \
              + '{:>4}'.format(jobSliceQueue[v].completionTime)

        print("|", a, "|", b, "    |", c, "    |", d, "   |", e, "      |", f, "|")
    
    print("-----------------------------------------------------------------------------------------")

# This outputs the average turnaround time to the montor. ---------------------------------------------
def outputAverageTurnAroundTime():
    print()
    print("The Average Turnaround Time is:", calculateAverageTurnaroundTime(), "milliseconds.")

# This outputs the footer. ----------------------------------------------------------------------------
def outputFooter():
    print()
    print("#########################################################################################")
    print()

# This outputs to the monitor the header, schedule table, average turnaroundtime, and footer. ---------
def outputResults():
    outputHeader()
    outputScheduleTable()
    outputAverageTurnAroundTime()
    outputFooter()

# This is where program execution begins. #############################################################

if __name__ == "__main__":

    # Open the file containing the list of jobs and read the contents into a list.
    jobFile = open("job.txt", "r")
    jobs = jobFile.readlines() # The jobs list temporarily holds the values from the file.
    jobFile.close()

    # Strip the items in the jobs list of their newline characters.
    for x in range(len(jobs)):
        jobs[x] = jobs[x][0:-1]
    
    # Calculate the number of jobs to do.
    numberOfJobs = len(jobs) // 2

    # Populate the job queue with jobs and set their respective attributes.
    for y in range(numberOfJobs):

        # Append a new job to the job queue.
        jobQueue.append(Job())

        # Set the job number of the new job.
        jobQueue[y].setJobNumber(jobs.pop(0))

        # Set the initial and remaining burst times of the new job.
        jobQueue[y].setInitialBurstTime(int(jobs.pop(0)))

    # Process all of the jobs in a Round-Robin fashion using a time quantum of two.

    while len(jobQueue) > 0:

            # Append a new job slice to the job slice queue.
            jobSliceQueue.append(JobSlice())

            # Set the job number of the new job slice to the job number of the current job.
            jobSliceQueue[jobSliceIndex].jobNumber = jobQueue[jobIndex].jobNumber

            # If the new job slice is not the first one in the job slice queue, set the job slice's
            # start time to the end time of the previous job slice.
            if jobSliceIndex != 0: 
                jobSliceQueue[jobSliceIndex].setStartTime(jobSliceQueue[jobSliceIndex - 1].endTime)

            # Set the job slice's initial burst time.
            jobSliceQueue[jobSliceIndex].setInitialBurstTime(jobQueue[jobIndex].initialBurstTime)

            # Slice the remaining burst time of the job in the job queue.
            jobQueue[jobIndex].calculateRemainingBurstTime()

            # Set the job slice's remaining burst time.
            jobSliceQueue[jobSliceIndex].setRemainingBurstTime(jobQueue[jobIndex].remainingBurstTime)

            # Calculate the job slice's end time.
            if jobQueue[jobIndex].finalSlice:
                timeAmount = jobSliceQueue[jobSliceIndex].remainingBurstTime
                jobSliceQueue[jobSliceIndex].remainingBurstTime = 0
                jobSliceQueue[jobSliceIndex].calculateEndTime(timeAmount)
            else:
                jobSliceQueue[jobSliceIndex].calculateEndTime(SLICE)

            # If the current job is finished, set its completion time, remove the job from the
            # job queue, and determine the appropriate next job index.
            if jobQueue[jobIndex].finalSlice == False:
                jobIndex = (jobIndex + 1) if jobIndex < (len(jobQueue) - 1) else 0
            else:
                jobSliceQueue[jobSliceIndex].setCompletionTime()
                jobQueue.pop(jobIndex)
                jobIndex = 0 if (jobIndex == len(jobQueue)) else jobIndex   

            jobSliceIndex += 1 

	# Output the header, schedule table, average turnaroundtime, and footer.
    outputResults()

# End of RoundRobinTwo Module #########################################################################