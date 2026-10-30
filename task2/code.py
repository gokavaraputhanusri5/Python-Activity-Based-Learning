
students = []
attendance = []
marks = []
events = []
allocations = []

# Classroom details using tuples
rooms = (("A101", 40), ("A102", 60), ("B201", 80))

while True:
    print("\n===== SMART CAMPUS MANAGEMENT =====")
    print("1. Add Student")
    print("2. Record Attendance")
    print("3. Enter Student Marks")
    print("4. Event Registration")
    print("5. Resource Allocation")
    print("6. Summary Report")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        branch = input("Enter Branch: ")
        students.append((sid, name, branch))
        print("Student added successfully!")

    elif choice == 2:
        sid = input("Enter Student ID: ")
        present = int(input("Enter Present Days: "))
        total = int(input("Enter Total Working Days: "))
        if total > 0 and 0 <= present <= total:
            attendance.append([sid, present, total])
            print("Attendance recorded!")
        else:
            print("Invalid attendance details!")

    elif choice == 3:
        sid = input("Enter Student ID: ")
        m1 = int(input("Enter Subject 1 Marks: "))
        m2 = int(input("Enter Subject 2 Marks: "))
        m3 = int(input("Enter Subject 3 Marks: "))
        if all(0 <= m <= 100 for m in [m1, m2, m3]):
            total = m1 + m2 + m3
            average = total / 3
            marks.append([sid, m1, m2, m3, total, average])
            print("Total:", total, "Average:", average)
        else:
            print("Invalid marks!")

    elif choice == 4:
        sid = input("Enter Student ID: ")
        event = input("Enter Event Name: ")
        events.append([sid, event])
        print("Event registration successful!")

    elif choice == 5:
        count = int(input("Enter Required Room Capacity: "))
        allocated = False
        for room, capacity in rooms:
            if count <= capacity:
                allocations.append((room, count))
                print("Allocated Room:", room)
                allocated = True
                break
        if not allocated:
            print("No suitable classroom available!")

    elif choice == 6:
        print("\n===== CAMPUS SUMMARY REPORT =====")

        print("\nStudent Records:")
        for sid, name, branch in students:
            print(sid, name, branch)

        print("\nAttendance Details:")
        for record in attendance:
            sid, present, total = record
            print(sid, present, "/", total,
                  "Percentage:", round(present / total * 100, 2), "%")

        print("\nMarks Details:")
        for record in marks:
            print(record)

        print("\nEvent Registrations:")
        for sid, event in events:
            print(sid, event)

        print("\nResource Allocations:")
        for room, count in allocations:
            print(room, "Capacity Used:", count)

    elif choice == 7:
        print("Thank you for using Smart Campus Management!")
        break

    else:
        print("Invalid choice! Please try again.")

