from fastapi import APIRouter

router = APIRouter()

students = [
    {
        "id": 1,
        "name": "Ludim Sánchez",
        "role": "senpai",
        "subjects": ["Programación Web", "Programación Python"],
        "email": "ludim@geggen.com"
    },
    {
        "id": 2,
        "name": "Mario Marin",
        "role": "senpai",
        "subjects": ["Programación Python", "Programación Orientada a Objetos"],
        "email": "mario.marin@educaruno.org"
    },
    {
        "id": 3,
        "name": "Néstor Navarro",
        "role": "senpai-kohai",
        "subjects": ["Programación Web", "Programación Python", "QA"],
        "email": "nesnava94@hotmail.com",
        "picture": ""
    },
]

def get_students_id():
    return map(lambda student: student.get('id', '-1'), students)

"""
Crear endpoints:
    Read        /students               GET
                /students/<student_id>
    Create      /students               POST
    Update      /students/<student_id>  PUT
    Delete      /students/<student_id>  DELETE
"""
@router.get("/students")
def get_students():
    if not students:
        return None
    return students

@router.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id > len(students):
        return None
    return students[student_id - 1]

@router.delete("/students/{student_id}")
def delete_student(student_id: int, function_name: str):
    #print("\n\t\tTESTING: ", function_name)
    #print("STUDENT", student_id, type(student_id))
    #print(students)
    if not students:
        return None
    if type(student_id) != int:
        return "Wrong datatype: student_id"

    if student_id > len(students):
        print("ESTUDIANTE NO EXISTE")
        return False

    position_student_id = student_id - 1
    #print("position_student_id", position_student_id)
    del students[position_student_id]
    #print("DD.BB.", students)
    return True


@router.post("/students")
def create_student(id,name,role,subjects,email,picture):
    new_student={
        "id": new_id,
        "name": new_name,
        "role": role,
        "subjects": subjects,
        "email": email,
        "picture": picture
    }
    for student in students:
        if students["id"] == new_student["id"] or students["name"] == new_student["name"] or students["email"] == new_student["email"]:
            return "Error: Student already exists"
        else:
            students.append(new_student)
            return True

    pass

@router.put("/students/{student_id}")
def edit_student(student_id):

    pass
