import csv
class Student:
    def studentdetails(self):
        with open("student.csv","a",newline="") as file:#if file doesnt exist it is created,newline says to write data in new line
            a=csv.writer(file)#csv.writer enables writing for csv
            a.writerow(["studentId","name"])#writerow write data in same row
            self.studentId=int(input("Enter id:"))
            self.name=input("Enter Name:")
            a.writerow([self.studentId,self.name])
            print("student data created")
    def display(self):
        self.studentId1=(input("enter id:"))
        self.name1=input("enter name:")
        with open("student.csv",'r',newline="") as file:#open file in reader syntax:with open as file_name:
            read=csv.DictReader(file) #dict reader used to read data
            for row in read:
                print(row['studentId']==self.studentId1)
                if row["studentId"]==self.studentId1 and row["name"]==self.name1:
                    print("Welcome")
                else:
                    print("Invalid")
login=Student()
#login.studentdetails()
login.display()


