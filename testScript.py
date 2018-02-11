from matrix.models import Matrix

'''
Ax = B
A = a_matrix
B = b_matrix
'''

a_matrix = ["zad1_a.txt", "zad2_a.txt", "zad3_a.txt", "zad4_a.txt", "zad5_a.txt"]
b_matrix = ["zad1_b.txt", "zad2_b.txt", "zad3_b.txt", "zad4_b.txt", "zad5_b.txt"]

for i in range(0, len(a_matrix)):
    """
        For all matrices calculate LU, LUP, forward and backward substitution
    """

    try:
        matrix = Matrix.fromtextfile("./test_files/" + a_matrix[i])
        b = Matrix.fromtextfile("./test_files/" + b_matrix[i])
    except FileNotFoundError:
        print("Missing file/s {}, {}...\n".format(a_matrix[i], b_matrix[i]))
        continue

    print("\n\n**********{} + {}**********\n".format(a_matrix[i], b_matrix[i]))

    try:
        print("############LU:############")
        matrix.lu()
        print("A:")
        print(str(matrix))
        matrix.forward_substitution(b)
        print("\n############LU: Forward substitution:####")
        print("Y:")
        print(str(b))
        matrix.back_substitution(b)
        print("\n############LU: Backward substitution:####")
        print("X:")
        print(str(b))
        print("############END############\n\n")

    except Exception as err:
        print(err)

    try:
        # Reload matrices
        matrix = Matrix.fromtextfile("./test_files/" + a_matrix[i])
        b = Matrix.fromtextfile("./test_files/" + b_matrix[i])

        print("############LUP:############")
        matrix.lup()
        print("A:")
        print(str(matrix))
        matrix.forward_substitution(b)
        print("\n############LUP: Forward substitution:############")
        print("Y:")
        print(str(b))
        matrix.back_substitution(b)
        print("\n############LUP: Backward substitution:############")
        print("X:")
        print(str(b))
        print("############END############\n\n")

    except Exception as err:
        print(err)

