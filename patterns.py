1. Print Star Pattern
*
**
***
****
*****
for i in range(5):
  for j in range(i+1):
        print("*",end="")
    print()
  
for i in range(1,int(input())+1):
    print("@"*i,end='')
    print()
2. Print Reverse Star Pattern
*****
****
***
**
*
  for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()

for i in range(5,0,-1):
    print("*"*i,end='')
    print()
  
3. Multiplication Grid
1 2 3
2 4 6
3 6 9
for i in range(1,4):
    for j in range(1,4):
        print(j*i,end="")
    print()
4. Print Triangle of Numbers
4.1
1
12
123
1234

for i in range(4):
    for j in range(i+1):
        print(f"{j+1}",end="")
    print()
4.2
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()

for i in range(1,6):
    print(f"{i} "*i,end="")
    print()

5. Print Floyd's Triangle
1
2 3
4 5 6
7 8 9 10

n=1
for i in range(1,5):
    for j in range(1,i):
        print(n,end=" ")
        n+=1
    print()
6.Alphabetic Pattern 
6.1
A
A B
A B C
A B C D
A B C D E

for i in range(1,6):
     for j in range(i):
          print(chr(65+j),end=' ')
        
     print()

6.2
a 
a b 
a b c 
a b c d 
a b c d e 
for i in range(1,6):
     for j in range(i):
          print(chr(97+j),end=' ')
        
     print()
  
6.3
a 
b b 
c c c 
d d d d 
e e e e e 
for i in range(5):
     for j in range(i+1):
          print(chr(97+i),end=' ')
        
     print()
6.4
A 
B B 
C C C 
D D D D 
E E E E E 

for i in range(5):
     for j in range(i+1):
          print(chr(65+i),end=' ')        
     print()

7. Inverted Number Traingle
7.1
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

7.2
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

7.3
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 

for i in range(6):
    for j in range(5,i,-1):
        print(j,end=" ")
    print()






