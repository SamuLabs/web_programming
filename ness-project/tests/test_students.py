from routers.students import *
import random
import unittest

class TestStudents(unittest.TestCase):
    """
    def test_get_students(self):
        students = get_students()
        self.assertIsNotNone(students)

    def test_get_student_not_exist(self):
        student_id = 4
        student = get_student(student_id)
        self.assertIsNone(student)
    
    def test_get_student_exist(self):
        student_id = 1
        student = get_student(student_id)
        self.assertIsNotNone(student)
    """
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

    """
    def test_delete_student_empty_database(self):
        student_id = 1
        student = delete_student(student_id)
        self.assertEqual(student, "Empty student's database")

    def test_get_students_id(self):
        ids = get_students_id()
        self.assertIsNotNone(ids)
    """

    # CREATE
    # Caso 1: True cuando usuario es creado
    # Caso 2: False cuando usuario (email) ya existe

    # PUT
    # Caso 1: True cuando usuario fue actualizado y existe
    # Caso 2: False cuando usuario no existe