students=["Mohit","Rohit","Ram","John","Fred","Ishaan","Shreya","Rishabh","Rahul"]
print(students)
print("The number of students in the class is ",len(students))
print(students[0])
print(students[-1])
print(students[0:4])
students.append("Sachin")
students.remove("Shreya")
students.sort()
print(students)
students.reverse()
print(students)
teacher={"name":"Praveen","Subject":"Maths","Experience":"8 years"}
print("The subject that the teacher teaches is", teacher["Subject"])
print("The teacher has ",teacher.get("Experience"))


