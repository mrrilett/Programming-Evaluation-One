#list of strings
people = ["Teacher", "Student", "Parent", "Principal"]
#list of numbers
grades = [76, 84, 91, 52]
#you can mix
things = ["car",  54, True, "hello"]

#indexing with []
print(people[0]) 

#adding items from a list together
mixedThings = ["hello", 4, 5, "bye", 7]
total = mixedThings[1] + mixedThings[2]
print(total)

#find the length of a list
people = ["p0", "p1", "p2", "p3"]
theLength = len(people)
print(theLength)

import random
studentList = ["sdf", "sdfdsf", "sdfsdf", "dffds", "dsf"]
x = random.randint(0, len(studentList))

print(studentList[x+1])
