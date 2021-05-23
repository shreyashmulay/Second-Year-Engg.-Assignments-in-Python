"""
Write a Python program for department library which has N books, write functions for following:
1)	Delete duplicate entries.
2)	Display books in ascending order based on cost of books.
3)	Count number of books with cost more than 500.
4)	Copy books in a new list which has cost less than 500.
"""
from array import*

Title=[[],[],[],[],[],[],[],[]]
cost=[[],[],[],[],[],[],[],[]]
cnt=0
temp1=0
temp2=0

a=int(input("Enter number of inputs you are giving (should beless than 6):"))
n=a
c=0
disT=[[],[],[],[],[],[]]
for i in range(0,n):
        Title[i]=input("Enter Title:")
        cost[i]=input("Enter cost :")
for i in range(n):
	print(Title[i],cost[i])
#delete duplicate entries
for i in range(0,n):
	for j in range(i+1,n):
		if(Title[i]==Title[j]):
			Title[i]
			Title.pop(j)
			cost.pop(j)
			c=c+1
			
print("Duplicate Entries Are Detected and deleted ")
for i in range(n-c):
	print(Title[i],cost[i])
			
for i in range(0,n):
        for j in range(i+1,n):
        		x=cost[i]
        		y=cost[j]
        		if(x>y):
        			temp1=Title[i]
        			Title[i]=Title[j]
        			Title[j]=temp1
        			temp2=cost[i]
        			cost[i]=cost[j]
        			cost[j]=temp2
print("Books in ascending order based on their cost :")
for i in range(n-c):
	print(Title[i],cost[i])
for i in range(0,n):
	if(cost[i]>=500):
		cnt=1+cnt
print("Book having cost less than 500 RS. :")		
for i in range(0,n):
	if(cost[i]<500):
		print(" -->",Title[i],cost[i])
print("Books having cost greater than 500 RS. :",cnt-c)

               
"""
***********OUTPUT*****************

Enter number of inputs you are giving (should beless than 6):4
Enter Title:C++
Enter cost :510
Enter Title:Python
Enter cost :450
Enter Title:Swift
Enter cost :600
Enter Title:Java
Enter cost :400
C++ 510   
Python 450
Swift 600
Java 400
Duplicate Entries Are Detected and deleted
C++ 510
Python 450
Swift 600
Java 400
Books in ascending order based on their cost :
Java 400
Python 450
C++ 510
Swift 600
"""