#-------------------------------------------
# SIMPLEX
# Luis Manuel Roman Garcia 
# Maria Fernanda Mora Alba
#-------------------------------------------

#-------------------------------------------
# Librerias utlizadas
#-------------------------------------------
import numpy as np
import numpy.matlib
import time

#-------------------------------------------
# Funciones
#-------------------------------------------

#-------------------------------------------
# pivot: lleva a cabo el proceso de 
# entrada y salida de variables de la base
# asi como actualizacion de coeficientes del tabloide
#-------------------------------------------
def pivot(tableau):
    tab_size = tableau.shape
    z        = tableau[-1, :]
    # Obtenemos el indice de la columna con el costo reducido 
    # mas grande
    enter_index = np.where(z[0] == np.min(z[0]))[1].item(0)
    coef        = np.divide(tableau[:-1,-1], tableau[:-1, enter_index])
    # Obtenemos el indice del renglon de salida y lo utilizamos
    # como pivote
    positive_coef = coef[np.where(coef >= 0)[0]]
    min_pos_coef  = positive_coef[0][np.where(positive_coef[0] == np.min(positive_coef))[0].item(0)][0].item(0)
    leave_index   = np.where(coef == min_pos_coef)[0].item(0)
    pivot         = np.divide(tableau[leave_index, :], tableau[leave_index, enter_index])
    # Llevamos a cabo reduccion gausiana usando como pivote
    # el renglon del calculo anterior
    for i in range(tab_size[0]):
        tableau[i, :] = tableau[i, :] - tableau[i, enter_index]*pivot
    tableau[leave_index, :] = pivot
    return tableau

#-------------------------------------------
# simplex: recibe la matriz y el vector de 
# restricciones asi como los coeficientes de la 
# funcion objetivo. lleva a cabo el proceso de 
# pivoteo dentro de un loop hasta llegar a un optimo
# regresa un arreglo el tabloide final y el valor de la funcion objetivo.
#-------------------------------------------
def simplex(A,b,z):
    # Verificamos si de entrada estamos en una solucion
    if np.sum(-z < 0) ==  0:
        print("La solucion es:")
    else:
        # Construimos el tabloide
        size_A = A.shape
        slack   = np.matlib.identity(size_A[0])
        shadow = np.hstack([-z, np.zeros(size_A[0] + 1)])
        tableau = np.hstack([A, slack,b])
        tableau = np.vstack([tableau, shadow])
        # Hacemos pivoteo hasta llegar a una solucion
        while np.sum(shadow < 0) != 0:
            tableau = pivot(tableau)
            shadow  = tableau[-1, :]
    return [tableau,tableau[-1,-1]]


#---------------------------------------------------------------
# Problemas de prueba
#---------------------------------------------------------------
# A es la matriz de restricciones, 
# z es la funcion objetivo
# b es el vector de restricciones
#---------------------------------------------------------------


# Problema de prueba 1 (clase)
A = np.array([[2,3],[4,1],[2,9]])
z = np.array([21,31])
b = np.array([[25],[32],[54]])
print("--------------------------------------------------------------------------------")
print("Ejemplo de clase")
print(simplex(A, b, z))
print("--------------------------------------------------------------------------------")


# Problema de prueba 2
A = np.array([[-1,1],[1,1],[2,5]])
z = np.array([4,6])
b = np.array([[11],[27],[90]])
print("--------------------------------------------------------------------------------")
print("Ejemplo 2")
print(simplex(A, b, z))
print("--------------------------------------------------------------------------------")

# Problema de prueba 3
A = np.array([[4,1,1],[2,3,1],[1,2,3]])
z = np.array([3,2,1])
b = np.array([[30],[60],[40]])
print("--------------------------------------------------------------------------------")
print("Ejemplo 3")
print(simplex(A, b, z))
print("--------------------------------------------------------------------------------")

