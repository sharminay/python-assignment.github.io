
print("Enter required subject GPA bellow (0 - 100) --> \n")

bangla = int(input("Enter Bangla GPA: "))
english = int(input("Enter English GPA: "))
math = int(input("Enter Math GPA: "))
science = int(input("Enter Science GPA: "))

total = bangla + english + math + science
avg = total / 4

if(avg > 90 and avg <= 100):
    print("\nGrade: A+\n")
elif(avg > 80 and avg <= 90):
    print("\nGrade: A\n")
elif(avg > 70 and avg <= 80):
    print("\nGrade: B\n")
elif(avg > 60 and avg <= 70):
    print("\nGrade: C\n")
elif(avg > 40 and avg <= 60):
    print("\nGrade: D\n")
elif(avg > 0 and avg <= 40):
    print("\nGrade: F\n")