"""
Write a python program to store first year percentage of students in an arr .Write Function for sorting arr of floating point numbers in ascending Order using:
1)Quick Sort and display Top five scorers:
"""

def partition(arr,low, high):
    pivot = arr[low]
    i= low + 1
    j= high

    while True:

        while i<=j and arr[j] >= pivot:
            j = j - 1

     
        while i<= j and arr[i] <= pivot:
            i = i+ 1

    
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]

        else:
           
            break

    arr[low], arr[j] = arr[j], arr[low]

    return j

def quick_sort(arr, low,high):
    if low>= high:
        return

    p = partition(arr, low,high)
    quick_sort(arr, low, p-1)
    quick_sort(arr, p+1,high)



percentage=[97.3,33.5,65.5,56.6,89.4,78.7,45.1,55.5,90.7]
print("Unsorted array is ",percentage)
n=len(percentage) 
quick_sort(percentage, 0, n- 1)
print("The sorted percentage array is : ",percentage)
a=1
for i in range(0,n):
	print("No.",a,"Ranker is",percentage[n-a])
	a=a+1  
	if(a==6):
		break  


""" 
******************OUTPUT********************

Unsorted array is  [97.3, 33.5, 65.5, 56.6, 89.4, 78.7, 45.1, 55.5, 90.7]
The sorted percentage array is :  [33.5, 45.1, 55.5, 56.6, 65.5, 78.7, 89.4, 90.7, 97.3]
No. 1 Ranker is 97.3
No. 2 Ranker is 90.7
No. 3 Ranker is 89.4
No. 4 Ranker is 78.7
No. 5 Ranker is 65.5
"""