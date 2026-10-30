
def minutes(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

courses = []
n = int(input("Enter number of courses: "))

for i in range(n):
    print("\nCourse", i + 1)
    name = input("Course name: ")
    day = input("Day: ")
    start = input("Start time (HH:MM): ")
    end = input("End time (HH:MM): ")
    room = input("Room number: ")

    courses.append((name, day, start, end, room))

unavailable = [("R2", "Monday", "10:00", "12:00")]
conflict = False

for i in range(n):
    for j in range(i + 1, n):
        a, b = courses[i], courses[j]

        if a[1] == b[1]:
            if minutes(a[2]) < minutes(b[3]) and \
               minutes(b[2]) < minutes(a[3]):
                print("Time conflict:", a[0], "and", b[0])
                conflict = True

for c in courses:
    for u in unavailable:
        if c[4] == u[0] and c[1] == u[1]:
            if minutes(c[2]) < minutes(u[3]) and \
               minutes(u[2]) < minutes(c[3]):
                print("Room unavailable for:", c[0])
                conflict = True

if conflict:
    print("\nTimetable is Invalid!")
else:
    print("\nTimetable is Valid!")

