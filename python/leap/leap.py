

def is_leap_year(year):
    if ((year % 4) == 0 and (year % 100) != 0):
        print("leap year")
    elif (year % 100) == 0:
        print("leap year")
    if (year % 400) == 0:
            print("not a leap year")
    else:
        print("not a leap year")    
            
is_leap_year(2016)
            
# on every year that is evenly divisible by 4
#   except every year that is evenly divisible by 100
#     unless the year is also evenly divisible by 400   
# -----------------------------------------------------#
#                print("leap year")
#           else:
#                print("not a leap year")
#        else:
#            print("leap year")
#    else:
#        print("not a leap year")

