from routers.students import *
import random
import unittest

class TestStudents(unittest.TestCase):
    
    def test_delete_student_not_exist(self):
        student_id = 4
        student = delete_student(student_id, "test_delete_student_not_exist")
        self.assertFalse(student)

    def test_delete_student_exist(self):
        student_id = 1
        student = delete_student(student_id, "test_delete_student_exist")
        self.assertTrue(student)

    def test_delete_student_datatype_wrong(self):
        student_id = '3'
        student = delete_student(student_id, "test_delete_student_datatype_wrong")
        self.assertEqual(student, "Wrong datatype: student_id")

    def test_delete_student_database(self):
        for student_id in range(1, 4):
            student = delete_student(student_id, "test_delete_student_database")
        students = get_students()
        self.assertIsNone(students)

    # CREATE
    # Caso 1: True cuando usuario es creado
    def test_create_student(self):
        student_id = create_student(
            4,
            "Pollo Loco",
            "senpai_kohai",
            ["Programación Web", "Programación Python", "QA"],
            "ricopollito@hotmail.com",
            "")
        self.assertTrue(student_id)
    
    # Caso 2: False cuando usuario (email) ya existe
    def test_create_student(self):
        student_id = create_student(
            5,
            "Pollo Loco",
            "senpai_kohai",
            ["Programación Web", "Programación Python", "QA"],
            "nesnava94@hotmail.com",
            "")
        self.assertEqual(student_id, "Error: Student already exists")

    # PUT
    # Caso 1: True cuando usuario fue actualizado y existe
    # Caso 2: False cuando usuario no existe