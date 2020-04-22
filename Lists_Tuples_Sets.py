courses = ['hist', 'math', 'physics']

print(len(courses))

# we can access the last item doing this. -2 would be the one previous, so math.
print(courses[-1])

# remember, when doing ranges, it prints the index it starts and then the index it ends before hitting.

print(courses[:2])  # prints hist and math

# sends to the end of the list
courses.append('art')

print(courses)

# sends something to the 0 index or any other one you want
courses.insert(0, 'art')

print(courses)

# add values of other list to list

courses2 = ['phil', 'soc']

courses.extend(courses2)

print(courses)

courses.remove('phil')

print(courses)

# remove last value of the list
# this will also return the value of what is removed
coursesPopped = courses.pop()

print(courses)
print(coursesPopped)

courses.reverse()

print(courses)

# sorts a list alphabetically or numerically
courses.sort()

print(courses)

courses.sort(reverse=True)

print(courses)

# this lets us sort the course without mutating it at all
sorted_courses = sorted(courses)

print(sorted_courses)

# print min num or character from a list. also max can be done
print(min(courses))

# find the index value of an item in a list
print(courses.index('art'))

# true of false is an item in a list?

print('art' in courses)

# print all items in the list

for item in courses:
    print(item)

# to get the value and index of an item in the list use enumerate
# for courses in enumerate(courses):
#     print(courses)

# or do this and you can add where things start
for index, course in enumerate(courses, start=1):
    print(index, course)
