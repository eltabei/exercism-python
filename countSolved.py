import os

count = 0
for root, dirs, files in os.walk('.'):
    for d in dirs:
        if len(filter(lambda x: x.endswith(".py"), os.listdir(d))) > 1:
            count += 1
print "Solved: ", count
