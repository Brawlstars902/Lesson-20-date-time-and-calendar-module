import random
import time
def getRandomDate(StartDate,EndDate):
    print('Choosing a random date between',StartDate,'and',EndDate,'.')
    RandomGenerator=random.random()
    DateFormat = '%m/%d/%Y'
    
    StartTime=time.mktime(time.strptime(StartDate,DateFormat))
    EndTime=time.mktime(time.strptime(EndDate,DateFormat))
    
    Randomtime=StartTime+RandomGenerator*(EndTime-StartTime)
    RandomDate=time.strftime(DateFormat, time.localtime(Randomtime))
    return RandomDate
print('The random date between my birthday(15/04/2014) and Arhaan\'s birthday(26/03/2016)is',getRandomDate("15/4/2014" , "26/3/2016"))