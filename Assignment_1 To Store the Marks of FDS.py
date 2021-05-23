"""
Write a Python program to store marks scored in subject "Fundamental of Data Structure" by N students in the class.
write function to compute following:
1)  The average score of class.
2)  Highest score and lowest score of class.
3)  Count of students who were absent for the test.
4)  Display marks with highest frequency.
"""

m1=[]
from array import*
total=input("total no of students in class:")
fds_marks=array('i',[])
n=int(input("Student present for exam :"))
for i in range(n):
    fds_marks.append(int(input("enter marks:")))
print("")
print("Average no. of students:",sum(fds_marks)/(n))
m=max(fds_marks)
print("Highest marks scored in exam is :",m)
o=min(fds_marks)
print("Lowest marks scored in exam is :",o)
ab= int (total)- int(n)
print("The absent students for exam: ",ab)
#here we have to make function for higher frequency nos.
def most_frequent(fds_marks):
    return max(set(fds_marks), key = fds_marks.count)
print("Most frequent marks scored are: ",most_frequent(fds_marks))

"""
***********OUTPUT*****************

total no of students in class:10
Student present for exam :8
enter marks:25
enter marks:24
enter marks:23
enter marks:22
enter marks:21
enter marks:20
enter marks:19
enter marks:18

Average no. of students: 21.5       
Highest marks scored in exam is : 25
Lowest marks scored in exam is : 18 
The absent students for exam:  2    
Most frequent marks scored are:  18 
"""