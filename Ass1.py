#3372 20/09/21
#Ass1: Write a program in python to create student database using classes & objects & do the following operations:
#          - Add record
#          - Modify record
#          - Search record
#          - Display all
#          - Display particular record
#          - Delete record

L = []

class Student:
	
    def __init__(self, name, rollno, cnum, branch):
        self.name = name
        self.rollno = rollno
        self.cnum = cnum
        self.branch = branch
        
    def accept(self):
        name = input("Student Name: ")
        rollno = int(input("Roll no: "))
        cnum = input("C num: ")
        branch = input("Branch: ")
        ob = Student(name, rollno, cnum, branch)
        L.append(ob)

    def display(self, ob):
        print("------------------------")	
        print("Name : ", ob.name)
        print("Roll no: ", ob.rollno)
        print("C number : ", ob.cnum)
        print("Branch : ", ob.branch)
        print("------------------------\n")	
        	
    def search(self, rn):
        for i in range(L.__len__()):
            if(L[i].rollno == rn):
                return i	
        print("Roll no. not found")
        return -1
							
    def delete(self, i):
        o = L.pop(i)
        del o
        print("Record deleted successfully")

    def update(self):
        rn = int(input("Enter roll no. of the student to modify record: "))
        i = obj.search(rn)
        if i != -1:
            L[i].name = input("New Name: ")
            L[i].rollno = int(input("New Roll no: "))
            L[i].cnum = input("New C num: ")
            L[i].branch = input("New Branch: ")


obj = Student('', 0, '', '')

while True:
    print("******* STUDENT DATABASE OPERATIONS *******")
    print("0. Exit")
    print("1. Add a record")
    print("2. Modify a record")
    print("3. Search a record")
    print("4. Display all records")
    print("5. Delete a record")
    ch = input("Enter your choice: ")
    print("___________________________________________\n")	

    if ch == '1':
        obj.accept()

    elif ch == '2':
        obj.update()

    elif ch == '3':
        rn = int(input("Enter roll no. of the student to search record: "))
        i = obj.search(rn)
        if i != -1:
            obj.display(L[i])

    elif ch == '4':
        if len(L) == 0:
            print("Student Database is empty.")
        else:
            print("******* STUDENT DATABASE ********")
            i = 1
            for l in L:
                print("Record #"+str(i))
                obj.display(l)
                i += 1

    elif ch == '5':
        rn = int(input("Enter roll no. of the student to delete record: "))
        i = obj.search(rn)
        if i != -1:
            obj.delete(i)

    elif ch == '0': 
        print("******** PROGRAM END **********")
        break

    else:
        print("Invalid choice")

