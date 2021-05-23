"""
Write a python program to store first year percentage of students in an array .Write Function for sorting array of floating point numbers in ascending Order using:
1) SELECTION SORT:
2) BUBBLE   SORT and display Top five scorers:
"""

from array import*
def selection_sort(Arr,n):
    temp=0
    for i in range (0,n):
        i1=i
        
        for j in range(i+1,n):
        
            if((Arr[i1])>(Arr[j])):
                i1=j


        #swaping element of i1 th location because on that location smallest no is present  in array;

        temp=Arr[i1]
        Arr[i1]=Arr[i]
        Arr[i]=temp
    return Arr

def bubble_sort(arr,n):
    temp=0
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print("The sorted Percentage by Using Bubble sort is",arr)
    j=5
    for i in range (n-5,n):
        print("No. ",j," Ranker is",arr[i])        
        j=j-1

#main function

per=[97.3,33.5,65.5,56.6,89.4,78.7,45.1,55.5,90.7]

n=(len(per))

print("The sorted Percentage by Using Selection sort is",selection_sort(per,n))
bubble_sort(per,n)


"""
*****************OUTPUT***********************
The sorted Percentage by Using Selection sort is [33.5, 45.1, 55.5, 56.6, 65.5, 78.7, 89.4, 90.7, 97.3]
The sorted Percentage by Using Bubble sort is [33.5, 45.1, 55.5, 56.6, 65.5, 78.7, 89.4, 90.7, 97.3]
No.  5  Ranker is 65.5
No.  4  Ranker is 78.7
No.  3  Ranker is 89.4
No.  2  Ranker is 90.7
No.  1  Ranker is 97.3
"""
    
