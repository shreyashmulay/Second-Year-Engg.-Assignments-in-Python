"""
Write a Python program to compute following computation on matrix:
1)	Addition of two matrix.
2)	Substraction of two matrix.
3)	Transpose of two matrix.
4)	Multiplication of two matrix.
"""

m1=[]
m2=[]

result=[[0,0,0],[0,0,0,],[0,0,0]]
n=int(input("Enter matrix size="))
for i in range(n):
    row=[]
    for j in range(n):
        print("Enter Element for m1=",i+1,j+1)
        temp=int(input())
        row.append(temp)
    m1.append(row)

for i in range(n):
    row=[]
    for j in range(n):
        print("Enter Element for m2= ",i+1,j+1)
        temp=int(input())
        row.append(temp)
    m2.append(row)
print("Our matrices are:")
for j in range(0,3):      
	print(m1[j][0],m1[j][1],m1[j][2])
print("    ")	
for j in range(0,3):
	print(m2[j][0],m2[j][1],m2[j][2])
print("  ")
print("Multiplication is :")
for i in range(3):
   for j in range(3):
       for k in range(3):
           result[i][j] += m1[i][k] * m2[k][j] 
for j in range(0,3):       
	print(result[j][0],result[j][1],result[j][2])	
for i in range(0,3): 
	for j in range(0,3): 
		result[i][j]=(m1[i][j])+(m2[i][j])	
print("The Addition is :")
for j in range(0,3):   
	print(result[j][0],result[j][1],result[j][2])		

for i in range(0,3): 
	for j in range(0,3): 
		result[i][j]=(m1[i][j])-(m2[i][j])
print("The Substraction is :")
for j in range(0,3):      
	print(result[j][0],result[j][1],result[j][2])

for i in range(0,3): 
	for j in range(0,3): 
		result[i][j]=m1[j][i]	
print("The Transpose of m1 is :")
for j in range(0,3):       
	print(result[j][0],result[j][1],result[j][2])
								
for i in range(0,3): 
	for j in range(0,3): 
		result[i][j]=m2[j][i]	
print("The Transpose of m2 is :")
for j in range(0,3):       
	print(result[j][0],result[j][1],result[j][2])

		
"""
***********OUTPUT*****************

Enter matrix size=3
Enter Element for m1= 1 1
1
Enter Element for m1= 1 2
2
Enter Element for m1= 1 3
3
Enter Element for m1= 2 1
4
Enter Element for m1= 2 2
5
Enter Element for m1= 2 3
6
Enter Element for m1= 3 1
7
Enter Element for m1= 3 2
8
Enter Element for m1= 3 3
9
Enter Element for m2=  1 1
1
Enter Element for m2=  1 2
2
Enter Element for m2=  1 3
3
Enter Element for m2=  2 1
4
Enter Element for m2=  2 2
5
Enter Element for m2=  2 3
6
Enter Element for m2=  3 1
7
Enter Element for m2=  3 2
8
Enter Element for m2=  3 3
9
Our matrices are:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Multiplication is :
30 36 42
66 81 96
102 126 150
The Addition is :
2 4 6
8 10 12
14 16 18
The Substraction is :
0 0 0
0 0 0
0 0 0
The Transpose of m1 is :
1 4 7
2 5 8
3 6 9
The Transpose of m2 is :
1 4 7
2 5 8
3 6 9
"""