students=[]
present=0
absent=0
for i in range(5):
    students=input(f"Enter Student {i+1} Name: ")
    att=int(input("if student  present 1 or absent 0:"))
    if att==1:
        present+=1
    else:
        absent+=1

print("====Attendance Report====")
print("Presentee: ",present)
print("Absentee :",absent)
