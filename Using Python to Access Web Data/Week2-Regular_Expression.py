import re
try:
    file1 = open("regex_sum_989261.txt")
except:
    print("File cannot be open")
    quit()
Sum = 0
for line in file1:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers) < 1:
        continue
    else:
        for number in numbers:
            Sum = Sum + float(number)
print(int(Sum))
