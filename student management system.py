print("*" * 60)
print("\t" * 5, "STUDENT MANAGEMENT SYSTEM", "\n")
print("*" * 60)

D1 = {}
ans = "Y"

while ans.upper() == "Y":
    print("Press 1. Create Dictionary having RN as Key and {Name: Marks} as Value.")
    print("Press 2. Display information of all students.")
    print("Press 3. Display students whose percentage is less than 90.")
    print("Press 4. Display students whose percentage is between 80 and 90.")
    print("Press 5. Search student by Roll Number.")
    print("Press 6. Search student by Name.")
    print("Press 7. Delete student by Roll Number.")
    print("Press 8. Delete student by Name.")
    print("Press 9. Update student by Roll Number.")
    print("Press 10. Update student by Name.")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        N = int(input("Enter how many students' info: "))

        for i in range(N):
            RN = int(input("Enter RN: "))
            Name = input("Enter Name: ")
            Marks = []

            for j in range(5):
                mrk = int(input("Enter marks: "))
                Marks.append(mrk)

            D1[RN] = {Name: Marks}

        print(D1)

    elif ch == 2:
        if len(D1) == 0:
            print("Kindly create Dictionary First i.e. choose option 1 first")
        else:
            for i in D1:
                print(i, "\t", D1[i])

    elif ch == 3:
        if len(D1) == 0:
            print("Kindly create Dictionary First i.e. choose option 1 first")
        else:
            for i in D1:
                name = list(D1[i].keys())[0]
                marks = D1[i][name]
                perc = (sum(marks) / 500) * 100

                if perc < 90:
                    print(i, "\t", D1[i])

    elif ch == 4:
        if len(D1) == 0:
            print("Kindly create Dictionary First i.e. choose option 1 first")
        else:
            for i in D1:
                name = list(D1[i].keys())[0]
                marks = D1[i][name]
                perc = (sum(marks) / 500) * 100

                if perc > 80 and perc < 90:
                    print(i, "\t", D1[i])

    elif ch == 5:
        if len(D1) == 0:
            print("Kindly create Dictionary First i.e. choose option 1 first")
        else:
            rno = int(input("Enter Roll No. to search: "))

            if rno in D1:
                print(rno, "\t", D1[rno])
            else:
                print("Sorry! record not found")

    elif ch == 6:
        if len(D1) == 0:
            print("Kindly create Dictionary First i.e. choose option 1 first")
        else:
            name = input("Enter Name to Search: ")
            found = False

            for rno in D1:
                student_name = list(D1[rno].keys())[0]

                if name.lower() == student_name.lower():
                    print(rno, "\t", D1[rno])
                    found = True

            if not found:
                print("Sorry! record not found")

    elif ch == 7:
        if len(D1) == 0:
            print("Kindly create Dictionary First i.e. choose option 1 first")
        else:
            rno = int(input("Enter Roll No. to delete: "))

            if rno in D1:
                del D1[rno]
                print("Record deleted successfully")
            else:
                print("Sorry! record not found")

    elif ch == 8:
        if len(D1) == 0:
            print("Kindly create Dictionary First i.e. choose option 1 first")
        else:
            name = input("Enter Name to delete: ")
            found = False

            for rno in list(D1.keys()):
                student_name = list(D1[rno].keys())[0]

                if name.lower() == student_name.lower():
                    del D1[rno]
                    found = True
                    print("Record deleted successfully")
                    break

            if not found:
                print("Sorry! record not found")

    elif ch == 9:
        if len(D1) == 0:
            print("Kindly create Dictionary First i.e. choose option 1 first")
        else:
            rno = int(input("Enter Roll No. to update: "))

            if rno in D1:
                print("Enter New Details")
                Name = input("Enter Name: ")
                Marks = []

                for j in range(5):
                    mrk = int(input("Enter marks: "))
                    Marks.append(mrk)

                D1[rno] = {Name: Marks}
                print("Record updated successfully")
            else:
                print("Sorry! record not found")

    elif ch == 10:
        if len(D1) == 0:
            print("Kindly create Dictionary First i.e. choose option 1 first")
        else:
            name = input("Enter Name to update: ")
            found = False

            for rno in list(D1.keys()):
                student_name = list(D1[rno].keys())[0]

                if name.lower() == student_name.lower():
                    print("Enter New Details")
                    NewName = input("Enter Name: ")
                    Marks = []

                    for j in range(5):
                        mrk = int(input("Enter marks: "))
                        Marks.append(mrk)

                    D1[rno] = {NewName: Marks}
                    found = True
                    print("Record updated successfully")
                    break

            if not found:
                print("Sorry! record not found")

    else:
        print("Invalid choice entered, please press between 1-10")

    ans = input("Wish to continue? Y/N: ")
