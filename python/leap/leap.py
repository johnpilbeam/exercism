year = input("Enter year: ");

def is_leap_year():
    if((year%4 == 0) and (year%100 != 0)):
        is_leap_year == True
    elif((year%100 == 0) and (year%400 == 0)):
        is_leap_year == True
    elif(year%400 == 0):
        is_leap_year == True
    else:
        is_leap_year == False

if is_leap_year == True:
    print("leap year!")
if is_leap_year == False:
    print("not a leap year!")
