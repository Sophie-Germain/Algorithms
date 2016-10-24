#Maria Fernanda Mora Alba, 103596
#Analisis de Algoritmos
#Programacion dinamica

####################################################################################
#Problema de la mochila TOPDOWN

import numpy as np
#definimos los vectores de pesos y utilidades de cada objeto, asi como la capacidad total de la mochila
weight = np.array([11,7,5,4,3,3,3,2,2,2,2,1])
util = np.array([20,10,11,5,25,50,15,12,6,4,5,30])
W = 20
n = len(weight)
table = -1*np.ones((n + 1, W + 1))  # tabla que me guarde los maximos


######PLANTEAMIENTO#####
#dividimos el problema en subproblemas en donde cada uno consiste en decidir si metemos o no el objeto i
#la decision de meterlo o no estara en funcion de cuanta utilidad nos reporte
#resolvemos el problema usando recursividad y el principio de optimalidad de Bellmann, de modo que 
#knapsack(i,w) la definimos como la utilidad maxima HASTA el objeto i (primer, segundo, ...,iesimo objeto
#con una capacidad disponible en la mochila de w para el objeto i.
#entonces knapsack(i,w) sera el maximo hasta el objeto i-1 metiendo o no el objeto i (si cabe)

######RUTINA###########
def knapsack_top(i, w):
    if i == -1 :
        return 0
    else:
        if weight[i] >= w:     #no cabe el objeto i
            if table[i, w] < 0:  #no se ha calculado, entonces lo guardo y lo regreso
                table[i, w] = knapsack_top(i - 1, w)
                return table[i, w]
            else:   #ya se calculo, lo busco y lo regreso 
                return table[i, w]
        else:   # si cabe, regreso el maximo
            if table[i, w] < 0:
                table[i, w] = max(knapsack_top(i - 1, w), 
                knapsack_top(i - 1, w - weight[i]) + util[i])
                return table[i, w]
            else:
                return table[i, w]

knapsack_top(n - 1, W)   #la solucion del problema es el maximo hasta el ultimo objeto con una capacidad total de W
   
        
#####################################################################################
#Problema de la mochila BOTTOMUP

def knapsack_bottom(n, W):
    m = np.zeros([n, W])
    for i in range(n):
        for j in range(W):
            if weight[i] <= j :
                m[i, j] = max(m[i - 1, j], util[i] + m[i - 1, j - weight[i]])
            else:
                m[i, j] = m[i - 1, j]
    return m[i, j]
    

knapsack_bottom(n, W) 

#####################################################################################
#Catalan numbers TOPDOWN

def cat_top(n):
    if n == 1 or n == 0:
        return 1
    else:
        s = 0
        if table2[n] < 0:
            for j in range(n+1)[1:]:
                s = s +  cat_top(j-1)*cat_top(n-j)
            table2[n] = s
        return table2[n]

#lo probamos
n = 7
table2 = -1*np.ones(n+1)
cat_top(n)

#####################################################################################
#Catalan BottomUp
def cat_bottom(n):
    cat=np.zeros(n+1)
    cat[0]=1
    for i in range(n+1)[1:]:
        s=0
        for j in range(i):
            s = s + cat[j]*cat[i-j-1]
        cat[i] = s
    return cat[n] 

#lo probamos
cat_bottom(5)
cat_bottom(6)
cat_bottom(7)
cat_bottom(10)
#####################################################################################
        