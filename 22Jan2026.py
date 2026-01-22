
def findCount():
    with open("C:\\Users\\cheta\\Desktop\\Python new cource\\Daily Tasks\\small.log","r") as file:
        errCount =0
        warnCount=0
        infoCount=0
        for line in file:
            if "ERROR" in line:
                errCount += 1
            elif "WARN" in line:
                warnCount += 1
            elif "INFO" in line:
                infoCount += 1
        print(errCount)    
        print(warnCount)  
        print(infoCount)  


def fetchDataByDay(Date):
    with open("C:\\Users\\cheta\\Desktop\\Python new cource\\Daily Tasks\\small.log","r") as file:
        for line in file:
            logDate=line[1:11]
            if(logDate==Date):
                print(line)

def fetchDataByDate(start,end):
    with open("C:\\Users\\cheta\\Desktop\\Python new cource\\Daily Tasks\\small.log","r") as file:
        for line in file:
            logDate=line[1:11]
            if(logDate>=start and logDate<=end):
                print(line)

def fetchDataByTime(Date,start,end):
    with open("C:\\Users\\cheta\\Desktop\\Python new cource\\Daily Tasks\\small.log","r") as file:
        for line in file:
            logDate=line[1:11]
            logTime=line[12:20]
            if(logDate==Date and logTime>=start and logTime<=end):
                print(line)
        

while True:
    print("1.check count")
    print("2.Search by date")
    print("3.Search by date interval")
    print("4.Search by time interval")
    choice = int(input("enter your choice"))
    match choice:
        case 1: 
                findCount()
        case 2:
                Date=input("enter the date(yyyy-mm-dd)")
                fetchDataByDay(Date)
        case 3: 
                start = input("enter the starting date(yyyy-mm-dd)")  
                end=input("enter the end date(yyyy-mm-dd)")     
                fetchDataByDate(start,end)
        case 4: 
                Date=input("enter the  date(yyyy-mm-dd)")
                startTime = input("enter the starting time(hh:mm:ss)")  
                endTime=input("enter the end time(hh:mm:ss)")     
                fetchDataByTime(Date,startTime,endTime)
        case _ :
               print("enter the correct choice")


