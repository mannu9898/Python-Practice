monthDays = [0,31,28,31,30,31,30,31,31,30,31,30,31]
               


def count_leap_year(day,month,year):
    if month<=2:
        year = year - 1
    return (year/4-year/100+year/400)



def getdiff(day1,month1,year1,day2,month2,year2):
    n1 = year1*365 + day1

    for i in range(0,month1):
        n1 = n1 + monthDays[i]

    n1 = n1 + count_leap_year(day1,month1,year1)

    n2 = year2*365 + day2

    for i in range(0 , month2):
        n2 = n2 + monthDays[i]

    n2 = n2 + count_leap_year(day2,month2,year2)

    return n2-n1

    print (n2)
    print (n2-n1)


print(getdiff(1,1,2012,28,2,2012))
