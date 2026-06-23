1. Print Star Pattern
*
**
***
****
*****
for i in range(5):
  for j in range(i+1):
        print("*",end="")
    print("\n")
  

2. Print Reverse Star Pattern
*****
****
***
**
*
  for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("\n")

3. Multiplication Grid
1 2 3
2 4 6
3 6 9
for i in range(1,4):
    for j in range(1,4):
        print(f"{j*i} ",end="")
    print("\n")
4. Print Triangle of Numbers
1
12
123
1234

for i in range(4):
    for j in range(i+1):
        print(f"{j+1}",end="")
    print("\n")

5. Print Floyd's Triangle
1
2 3
4 5 6
7 8 9 10

n=1
for i in range(1,6):
    for j in range(1,i):
        print(n,end=" ")
        n+=1
    print("\n")


