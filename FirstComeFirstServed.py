###################################################################################################
# First Come First Served (FCFS) Algorithm Implementation
# ------------------------------------------------------------------------
# Mark Barros
# CS 4310 - Operating Systems
# 2021 Summer Semester - California Polytechnic State University
###################################################################################################

# These are data structures. ######################################################################

# This defines the job object. --------------------------------------------------------------------
class Job:

    # These are the object's data attributes.
    jobNumber = "Job 0" # (equals the value given in job.txt)
    burstTime = 0 # (equals the value given in job.txt)
    startTime = 0 # (equals 0 if first job in queue, otherwise equals end time of previous job)
    endTime = 0 # (start time plus burst time)
    completionTime = 0 # (equals end time in all cases)

    # These are the object's methods.
    def setJobNumber(self, jobNumber):
        self.jobNumber = jobNumber

    def setBurstTime(self, burstTime):
        self.burstTime = burstTime

    def setStartTime(self, start):
        self.startTime = start

    def calculateEndTime(self):
        self.endTime = self.startTime + self.burstTime

    def setCompletionTime(self):
        self.completionTime = self.endTime
    
# This defines a ready queue using a list object. -------------------------------------------------
jobQueue = []

# These are variables. ############################################################################
averageTurnaroundTime = 0
numberOfJobs = 0

# These are functions. ############################################################################

# This calculates the average turnaround time. ----------------------------------------------------
def calculateAverageTurnaroundTime():
    sumOfCompletionTimes = 0
    for w in range(len(jobQueue)):
        sumOfCompletionTimes += jobQueue[w].completionTime
    return "{:.2f}".format(sumOfCompletionTimes / numberOfJobs)

# This outputs the header. ------------------------------------------------------------------------
def outputHeader():
    print()
    print("#####################################################################################")
    print()
    print("First Come First Served (FCFS) Algorithm Implementation - By Mark Barros")
    print()

# This outputs the schedule table to the monitor. -------------------------------------------------
def outputScheduleTable():

    print("------------------------------------------------------------------------")
    print("| Job  # | Burst Time | Start Time | End Time |     Completion Time    |")
    print("------------------------------------------------------------------------")

    for v in range(len(jobQueue)):

        a = '{:>2}'.format(jobQueue[v].jobNumber)
        b = '{:>6}'.format(jobQueue[v].burstTime)
        c = '{:>6}'.format(jobQueue[v].startTime)
        d = '{:>5}'.format(jobQueue[v].endTime)
        e = jobQueue[v].jobNumber + " completed @" + '{:>4}'.format(jobQueue[v].completionTime)

        print("|", a, "|", b, "    |", c, "    |", d, "   |", e, "|")
    
    print("------------------------------------------------------------------------")

# This outputs the average turnaround time to the montor. -----------------------------------------
def outputAverageTurnAroundTime():
    print()
    print("The Average Turnaround Time is:", calculateAverageTurnaroundTime(), "milliseconds.")

# This outputs the footer. ------------------------------------------------------------------------
def outputFooter():
    print()
    print("#####################################################################################")
    print()

# This outputs to the monitor the header, schedule table, average turnaroundtime, and footer. -----
def outputResults():
    outputHeader()
    outputScheduleTable()
    outputAverageTurnAroundTime()
    outputFooter()

# This is where program execution begins. #########################################################

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

    # Calculate the range of values to iterate through.
    values = len(jobs) - 1

    # Populate the job queue with jobs and either set or calculate their data attributes.
    for y in range(values):
        if len(jobs) > 0:

            # Append a new job to the job queue.
            jobQueue.append(Job())

            # Set the job number of the new job.
            jobQueue[y].setJobNumber(jobs.pop(0))

            # Set the burst time of the new job.
            jobQueue[y].setBurstTime(int(jobs.pop(0)))

            # If it is not the first job in the job object queue, set the start time of the
            # new job to the end time of the last 
            if y != 0: 
                jobQueue[y].setStartTime(jobQueue[y - 1].endTime)

            # Calculate the end time of new job.
            jobQueue[y].calculateEndTime()

            # Set the completion time of the new job.
            jobQueue[y].setCompletionTime()

	# Output the header, schedule table, average turnaroundtime, and footer.
    outputResults()

# End of FirstComeFirstServed Module ##############################################################