import pandas as pd
# Creat Disconary
Student_grade = {  }


#  Adding Element
def add_Student(name,grade):
    Student_grade[name] = grade
    #[Aatif] = 100
    print(f"Added {name} With a {grade}")

    #Added sugar with a 100
    save_to_excel()


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
    save_to_excel()


# View All student

def display_all_student():
    if Student_grade:
        for name , grade in Student_grade.items():
            print(f"{name} : {grade}")
    else:
        print("No student found/added")


#Main Logic
def main():
    while True:
        print('\n STUDENT GRADE MANAGEMENT SYSTEM')
        print('1. Add Student')
        print('2. Update Student')
        print('3.Delete Student')
        print('4. View Student')
        print('5. Exit')

        choice = int(input("Enter your choice ="))

        if choice == 1:
            name = input("Enter Your Nmae =")
            grade = int(input("Enter Student Grade ="))
            add_Student(name , grade)
        
        elif choice == 2:
            name = input("Enter Your Nmae =")
            grade = int(input("Enter Student Grade ="))
            update_Student(name , grade)
        
        elif choice ==3:
            name = input("Enter Your Nmae =")
            delete_student(name)
        
        elif choice == 4:
            display_all_student()

        elif choice ==5:
            print("Closing the program . .")
            break
        else:
            print("Invalade Choose !")


def save_to_excel():
    df = pd.DataFrame(list(Student_grade.items()), columns=["Name", "Grade"])
    df.to_excel("student_grades.xlsx", index=False)
    print("Data saved to Excel successfully ")


main()


