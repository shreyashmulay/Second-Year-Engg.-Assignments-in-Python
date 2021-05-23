"""
write a python program to store roll numbers of students in array who attend training program in random order:
1):	write function for searching whether particular student attend training or not using linear search and sentinel search.
2):	write function for searching whether particular student attend training or not using Binary search and fibonacci search.
"""

from array import*

def li_se(roll,n,a):
	for i in range(n):
		if a==roll[i]:
			print("The no is found By Linear Search at location :",i)
			break
		if i==(n-1):
			roll.append(a)
			print("The no notfound, By Sentinel Search we added at last:",i+1)
def binary(roll,n,a):
	n=(len(roll))		
	for i in range(0,n):
    	    for j in range(i+1,n):
    	            if(roll[i]>roll[j]):
    	                    temp=roll[i]						
    	                    roll[i]=roll[j]
    	                    roll[j]=temp
	print("the sorted roll no:",roll)
	t=int(n/2)
	if(a==roll[t]):
		print("The no is found By Binary Search at location :",i)
	elif a>roll[t]:
	        for i in range(t,n):
	                if a==roll[i]:
	                        print("The number is found by Binary Search at location :",i)
	else:
	        for i in range(0,t):
	                if a==roll[i]:
	                        print("The number is found by Binary Search at location :",i)
                
#fibonacci
def fibonacci(roll,n,a):
	b=0
	a=1
	c=b+a
	offset=-1
	while(c<n):
		b=a
		a=c
		c=b+a
	
	while(c>1):
		i=min(offset+b,n-1)
		
		if(roll[i]<a):
			c=a
			a=b
			b=c-a
			offset=i
		elif(roll[i]>a):
			c=b
			a=a-b
			b=c-a
		else:
			print("The no is found by Fibonacci search at ",i)
			break

roll=array('i',[])
new=array('i',[])
roll=[10,9,11,12,24,25,2,8,13,35,42,44,40,3,1]
a=int(input("enter no you want to search :"))
n=(len(roll))
temp=0
li_se(roll,n,a)
binary(roll,n,a)
fibonacci(roll,n,a)

"""
***********OUTPUT*****************

enter no you want to search :3
The no is found By Linear Search at location : 13
the sorted roll no: [1, 2, 3, 8, 9, 10, 11, 12, 13, 24, 25, 35, 40, 42, 44]
The number is found by Binary Search at location : 2
The number is found by Fibonacci search at : 2
"""
