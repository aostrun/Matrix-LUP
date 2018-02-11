from unittest import TestCase
from matrix.models import Matrix
from decimal import Decimal



class MatrixTestCase(TestCase):


    def setUp(self):
        self.matrix = Matrix.fromtextfile("../test_files/test.txt")

    def test_init(self):


        tmp = [[12.5, 3.0, 9.0, 2.0], [4.0, 5.0, 6.0, 7.0], [8.0, 9.0, 10.0, 11.0]]
        matrix_test = Matrix(data=tmp)

        self.assertEqual(self.matrix, matrix_test)

    def test_add(self):

        matrix_expected = Matrix(data=[[13.5, 5.0, 12.0, 6.0], [8.0, 8.0, 8.0, 8.0], [9.1, 11.2, 13.3, 15.4]])

        matrix_test = Matrix(data=[[1.0, 2.0, 3.0, 4.0], [4.0, 3.0, 2.0, 1.0], [1.1, 2.2, 3.3, 4.4]])

        ans_matrix = self.matrix + matrix_test

        self.assertRaises(AttributeError, self.matrix.__add__, 5.0)

        self.assertEqual(ans_matrix, matrix_expected)

    def test_sub(self):

        matrix_expected = Matrix(data=[[11.5, 1.0, 6.0, -2.0], [0.0, 2.0, 4.0, 6.0], [6.9, 6.8, 6.7, 6.6]])

        matrix_test = Matrix(data=[[1.0, 2.0, 3.0, 4.0], [4.0, 3.0, 2.0, 1.0], [1.1, 2.2, 3.3, 4.4]])

        ans_matrix = self.matrix - matrix_test

        self.assertRaises(AttributeError, self.matrix.__sub__, 5.0)

        self.assertEqual(ans_matrix, matrix_expected)

    def test_mul(self):

        matrix_test = Matrix(data=[[1.0, 1.0], [2.0, 2.0], [3.0, 3.0], [4.0, 4.0]])
        matrix_expected = Matrix(data=[[53.5, 53.5], [60.0, 60.0], [100.0, 100.0]])

        matrix_expected_scalar = Matrix(data=[[41.25, 9.9, 29.7, 6.6], [13.2, 16.5, 19.8, 23.1], [26.4, 29.7, 33, 36.3]])

        ans_matrix = self.matrix * matrix_test
        ans_matrix_scalar = self.matrix * 3.3

        round(ans_matrix_scalar, 2)

        self.assertEqual(ans_matrix, matrix_expected)
        self.assertEqual(ans_matrix_scalar, matrix_expected_scalar)

    def test_lu_pivot_zero(self):
        matrix_test_A = Matrix(data=[[1, 1, 1], [1, 1, 3], [1, 3, 3]])
        matrix_test_b = Matrix(data=[[0.5], [2], [1]])

        self.assertRaises(ArithmeticError, matrix_test_A.lu)