# copy = {
#     "brand" : "chiya",
#     "size" : "A4",
#     "price" : "150"
# }
# print(copy["brand"])
# copy["brand"] = "gurukul"
# print(copy.items())


'''
Write a python program to create a dictionary of 5 students with name in the key and marks in the value. then perform:
1. Add a new students with their score.
2. Update the score of an existing students.
3. Delete a student from the dictionary.
4. Print the dictionary.
ps: Print the key and value in each step.
'''
student = {
    "Kavya" : 81,
    "Gauri" : 87,
    "Sangita" : 85,
    "Govinda" : 90,
    "Sangam" : 95,
    }
# add a new student with score
student["Milan"] = 93,
print(student)
#print key
for x in student:
    print(x)
#print values
for x in student.values():
    print(x)    
# update the score of an student
student.update({"kavya": 91})
print(student)
#print key
for x in student:
    print(x)
#print values
for x in student.values():
    print(x) 
# delete a student from the dictionary
del student["Sangita"]
print(student)
#print key
for x in student:
    print(x)
#print values
for x in student.values():
    print(x) 

