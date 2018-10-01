import datetime
import calendar

keyDaysOfyear = {1,2,3}
keyDaysOfyear.clear()

"""'

The runner part of the application simply calls a getDatePeriod method with Year, Month, Day and day arguments. Sample are provided.

This then call the 2 key methods
  - fillPeriodsForSpecificDate — passes in the date in question and populates a set keyDaysOfyear.
  - findPeriod — passes in the date in question.

The fillPeriodsForSpecificDate aims to fill a set (keyDaysOfyear) with the relevant start dates.

The fillPeriodsForSpecificDate method get the first day of the year, and then finds the day of week of that first day. Given that we can work out the first 
Saturday. Then we use a simple range and add all the days of years (as day of year simple number) — we have also added the first day of the year as well.

We also add the 1st days of the month — for the following 11 months (Feb to Dec).

The aim of this method is thus met — a field set with all the relevant start dates.

The find period methods then aims to find the period that the date falls into, and print the result. We get the day count for the date of interest — into specificDaysOfYearasCount

We iterate through a sorted version of the keyDaysOfyear, and see if the date is before the start of the period. 
If it is then we want the preious period. The end of the previous period will be 1 less than the start of the next. Once our specific date is less than a period found, we stop iterating.

We have a supporting method to trim the end period — if it a leap year then there are 366 days, otherwise it is just 365 days.

Finally, we simply print the result out in the required format.

"""


def fillPeriodsForSpecificDate(year, month, day):
    specificdate = datetime.datetime(year, month, day)
    #yearInQuestion = specificdate.strftime("%Y")
    firstDayOfYear = datetime.datetime(year, 1, 1)
    firstweekdayofYearNumber = firstDayOfYear.strftime("%w")
    firstSaturdayDayCount = 7 - int(firstweekdayofYearNumber)
    #keyDaysOfyear.add(firstweekdayofYearNumber)
    keyDaysOfyear.add(int("1"))
    for saturdaysDayCount in range(int(firstweekdayofYearNumber), 372, 7):
        keyDaysOfyear.add(saturdaysDayCount)

    for monthCount in range(2, 12):
        firstdayofMonthsDate = datetime.datetime(year, monthCount, 1)
        keyDaysOfyear.add(int(firstdayofMonthsDate.strftime("%j")))


def findPeriod(year, month, day):
    specificdate = datetime.datetime(year, month, day)
    specificDaysOfYearasCount = specificdate.strftime("%j")

    startofPeriodAsCount = 1
    endOfPeriodAsCount = 0
    #foundPeriod = False
    periodCount = -1
    for periodstart in sorted(keyDaysOfyear):
        periodCount += 1
        if (int(specificDaysOfYearasCount) < int(periodstart)):
            endOfPeriodAsCount = int(periodstart) -1
            #foundPeriod = True
            break

        else:
            startofPeriodAsCount = int(periodstart)


    # now need to trim for leap years
    if (endOfPeriodAsCount > 364):
        actualEndofYearCount = trimEndOfYear(year, endOfPeriodAsCount)
        endOfPeriodAsCount = actualEndofYearCount


    startofPeriodAsDate = datetime.datetime(year, 1, 1) + datetime.timedelta(startofPeriodAsCount - 1)
    endOfPeriodAsDate = datetime.datetime(year, 1, 1) + datetime.timedelta(endOfPeriodAsCount - 1)

    #print("Start of Period " + str(startofPeriodAsDate) + "+++ End of Period " + str(endOfPeriodAsDate) + "  +++ Period Count " + str(
    #    periodCount))

    print("Start of Period " + startofPeriodAsDate.strftime("%b") + "-"+""+startofPeriodAsDate.strftime("%d") + " +++ End of Period " +
          endOfPeriodAsDate.strftime("%b") + "-"+""+ endOfPeriodAsDate.strftime("%d") + "  +++ Period Count " + str(
        periodCount))

def trimEndOfYear(Year,endOfPeriodAsCount):
    if calendar.isleap(Year):
        return 366
    else:
        return 365

def getDatePeriod(inYear, inMonth, inDay):
    fillPeriodsForSpecificDate(int(inYear),int(inMonth), int(inDay))
    findPeriod(int(inYear), int(inMonth), int(inDay))

getDatePeriod("1993","01","01")
getDatePeriod("1993","01","12")
getDatePeriod("1993","01","15")
getDatePeriod("1993","01","19")
getDatePeriod("1993","12","31")
getDatePeriod("1993","01","12")
getDatePeriod("1993","01","01")
getDatePeriod("1993","12","31")
getDatePeriod("1993","12","31")
