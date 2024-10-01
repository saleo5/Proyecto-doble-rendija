import numpy as np
import math
"""
------ Libreria operaciones con numeros complejos
"""
# Version 1
def sumacpmx(c1, c2):
    """1: Adición de vectores complejos"""
    suma = []
    for i in range(0, len(c1)):
        suma.append(c1[i] + c2[i])
    return suma

def inversocpmx(c):
    """2: Inverso (aditivo) de un vector complejos."""
    inve = []
    for i in range(len(c)):
        inve.append(-c[i])
    return inve

def mult_esca_vect_cpmx(e,v):
    """3: Multiplicación de un escalar por un vector complejo."""
    mult = []
    for i in range(len(v)):
        mult.append(e * v[i])
    return mult

def suma_mat_complex(mat1,mat2):
    """4: Adición de matrices complejas."""
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "No son matrices compatibles"
    else:
        matrix = [[0 for i in range(len(mat1))] for j in range(len(mat1[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = mat1[i][j] + mat2[i][j]
        return matrix

def mat_inv_cpmx(mat):
    """5 :Inversa (aditiva) de una matriz compleja."""
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = -mat[i][j]
    return mat

def mat_mult_esc_cpmx(k, mat):
    """6: Multiplicación de un escalar por una matriz compleja."""
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = k * mat[i][j]
    return mat

def mat_traspone_cpmx(mat):
    """7: Transpuesta de una matriz/vector"""
    m = len(mat)
    n = len(mat[0])
    matrix = [[0 for i in range(m)] for j in range(n)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[j][i] = mat[i][j]
    return matrix

def neg_imag_matrix_cpmx(mat):
    """8: Conjugada de una matriz/vector"""
    dis = len(mat)
    dis2 = len (mat[0])
    for i in range(dis):
        for j in range(dis2):
            mat[i][j] = mat[i][j].conjugate()
    return mat

def adjunta_daga_cpmx(mat):
    """9: Adjunta (daga) de una matriz/vector"""
    return mat_traspone_cpmx(neg_imag_matrix_cpmx(mat))

def product_mat(mat1,mat2):
    """10: Producto de dos matrices (de tamaños compatibles)"""
    m1 = len(mat1)
    n1 = len(mat1[0])
    m2 = len(mat2)
    n2 = len(mat2[0])
    if n1 != m2:
        return "No son matrices compatibles"
    else:
        matri = [[0 for row in range(n2)] for col in range(m1)]
        for i in range(m1):
            for j in range(n2):
                for k in range(m2):
                    matri[i][j] += mat1[i][k] * mat2[k][j]
        return matri

def accion_mat(mat, vect):
    """11: Función para calcular la "acción" de una matriz sobre un vector."""
    matriz = np.array(mat)
    vector = np.array(vect)
    rest = np.dot(matriz,vector)
    return str(rest)

def produc_interno_vec(vector_1,vector_2):
    """12: Producto interno de dos vectores"""
    sum = 0
    if len(vector_1) != len(vector_2):
        return "No son vectores compatibles. "
    else:
        for i in range(len(vector_1)):
            sum+= vector_1[i]*vector_2[i]
    return sum

def norma_vector(vec):
    """13: Norma de un vector."""
    sum = 0
    for i in range(len(vec)):
        sum+=abs(vec[i])**2
        print(sum)
    return round((sum)**0.5, 2)

def distance_vect(vect_1, vect_2):
    """14: Distancia entre dos vectores."""
    resta = []
    for i in range(0, len(vect_1)):
        resta.append((vect_1[i] - vect_2[i]))
    ver = str(resta[0])
    val = []
    for i in range(len(ver)):
        if ver[i] == "+" or ver[i] == "-":
            val.append(ver[i-1])
            val.append(ver[i+1])
            break
    su = 0
    for i in range(2):
        su+=int(val[i])**2
    return round(su**0.5, 2)

def val_vec_prop_mat(mat):
    """15. Valores  y vectores propios de una matriz."""
    if len(mat) != len(mat[0]): return "No es una matriz cuadrada"
    matriz = np.array(mat)
    valores_propios, vectores_propios = np.linalg.eig(matriz)
    return "los valores propios para esta matriz o vector son {} y los vectores son {}".format(valores_propios, vectores_propios)

def mat_unita(mat):
    """16. Revisar si una matriz es unitaria."""
    long_f = len(mat)
    long_c = len(mat[0])
    if long_c != long_f:
        return "La matriz no es cuadrada"
    for i in range(long_f):
        for j in range(long_c):
            if i == j:
                if mat[i][j] == 1:
                    continue
            else:
                if mat[i][j] != 0:
                    return "No es unitaria"
    return "Si es matriz unitaria"

def mat_hermitiana(mat):
    """17. Revisar si una matriz es Hermitiana."""
    m = len(mat)
    n = len(mat[0])
    mat2 = mat_traspone_cpmx(mat)
    for row in range(m):
        for column in range(n):
            if mat[row][column] != (mat2[row][column]).conjugate():
                return "No es hermitiana"
    return "Es hermimtiana"


def prod_tense_mat(mat1, mat2):
    """18. Producto tensor de dos matrices/vectores."""
    m = len(mat1)
    n = len(mat2)
    m1 = len(mat1[0])
    n1 = len(mat2[0])
    fil = m * n
    col = n1 * m1
    matriz = [[0 for row in range(fil)]for column in range(col)]
    for j in range(fil):
        for k in range(col):
            matriz[j][k] = (mat1[j//n][k//n1] * mat2[j%n][k%n1])
    return matriz