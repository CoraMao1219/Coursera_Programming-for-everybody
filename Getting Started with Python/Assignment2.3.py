#2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#You should use input to read a string and float() to convert the string to a number.

hrs = input('Enter Hours:')
fhrs = float(hrs)
rate = input ('Enter Rate per Hour:')
frate = float(rate)
print ('Pay:', fhrs*frate)
