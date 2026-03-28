# Creat Disconary
Student_grade = {  }


#  Adding Element
def add_Student(name,grade):
    Student_grade[name] = grade
    #[Aatif] = 100
    print(f"Added {name} With a {grade}")
    #Added sugar with a 100


#Update a Student
def update_Student(name, grade):
    if name in Student_grade:
        Student_grade[name] = grade
        print(f"Added {name} With Marks are updated {grade}")
    else:
        print(f"{name} is not found !")


# Delete Student

def delete_student(name):
    if name in Student_grade:
        del Student_grade[name]
        print(f"{name} has been succesfully deleted")
    else:
        print(f"{name} is not found !")


# View All student