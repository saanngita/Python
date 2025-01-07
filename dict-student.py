student = {
    "Bob" : 55,
    "Alice" : 85,
    "Charlie" : 95,
    "David" : 75,
    "Eve" : 65,
}
student_name = input("Enter the name of the student to check their score:")
if student_name in student:
    print(f"{student_name} score is {student[student_name]}")
else:
    print(f"{student_name} is not found.")
score = input("Do you want to update score? yes or no")
if score == "yes":
  update_name = input("Enter the name of student to update.")
  if update_name in student:
    update_score = int(input("Enter score to update."))
    update_score = student.update({student_name : update_score})
  else:
    print(student_name,"not found.")
print("All students")
for student_name, student[student_name] in student.items():
#    score = student[student_name]
   print(student_name, student[student_name])

for x in student:
   print(f"{x} {student[x]}")
  
    



       





    

