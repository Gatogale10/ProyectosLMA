import itertools
import math


#Definimos la composition de las funciones

def producto(a,b1):

    '''
    :param a: Es una lista de longitud n
    :param b: Es una lista de longitud n
    :return: Una lista de la misma longitud
    '''
    c = []
    for i in range(len(a)):
        c.append(a[b1[i]])

    return c

def inversa(a):

    aux = [i for i in range(len(a))]
    j = 0



    for i in a:
        aux[i] = j
        j = j +1


    return aux


a = [3 , 1, 0 ,2]
b = [0 ,1 ,3, 2]

print(a)
invera = inversa(a)
print(invera)

print(producto(a,invera))

def Grupo_Simetrico(n):

    x = [i for i in range(n)]

    s_n = itertools.permutations(x)
    print(s_n)
    for perm in s_n:
        inver = inversa(perm)
        print(f"El inverso de {perm} es {inver}")

        print(f" Comprobacion {producto(perm,inver)}")



Grupo_Simetrico(4)

def iteracion(a,k):

    """

    :param a: Es una lista
    :param k: k es un natural
    :return: el producto de a k veces
    """

    res = a

    for i in range(1,k):
        res = producto(res,a)

    return res


def order(a):

    """

    :param a: Es una lista
    :return: el orden de a
    """

    identidad = [i for i in range(len(a))]

    for i in range(1,math.factorial(len(a))+1):
        order = iteracion(a,i)
        if order == identidad:
            return i


