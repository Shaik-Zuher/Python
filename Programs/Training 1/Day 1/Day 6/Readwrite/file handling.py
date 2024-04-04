#open function ---to open a file ,file may be csv,text
#open syntax:f=open(filename,mode,newline="")
#modes---:r:open existing file
#         w:write a file,but data is overriden
#         a:writes data in file,data not overridden
#         r+:read and write file
#         w+:write and read a file,but data is overriden
#         a+:writes and read data in file,data not overridden
#functions used are f.read(),f.write(),f.close()(f is vraible where file is stored)
#f.writelines([])--writes multiple lines,passed value must be list containing strings
import csv#importing csv file
f=open("student.csv","a",newline="")#if file doesnt exist it is created,newline says to write data in new line
a=csv.writer(f)#csv.writer enables writing for csv
a.writerow(["studentId","name","phone"])#writerow write data in same row
studentId=int(input("Enter id:"))
name=input("Enter Name")
phone=input("enter phone:")
a.writerow([studentId,name,phone])
print("student data created")

