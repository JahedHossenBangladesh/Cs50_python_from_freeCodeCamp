a_list=["Hermione","Harry","Ron","Draco"]
houses =["Gryffindor","Gryffindor","Gryffindor","Slytherin"]

students={
    "hermione":"Gryor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    }
# print(students["hermione"])

for student in students:
    print(student, students[student],sep=(", "))