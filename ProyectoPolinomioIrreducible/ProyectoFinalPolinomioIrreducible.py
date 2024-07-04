# Jorge Gael Lopez Figueras
# Proyecto extensión de campos

#Importamos las librerias a utilizar
import itertools
import math
from itertools import product

#Funcion que multiplica dos polinomios
def mult_polinom_Zp(poly1, poly2,p):
    # Inicializar el arreglo para almacenar el polinomio resultante
    result = [0] * (len(poly1) + len(poly2) - 1)

    # Multiplicar los polinomios
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += ((poly1[i] * poly2[j]) % p)



    return result

def Monico(v1,p):

    a = re2(v1)

    n = (a**(p-2))

    for i in range(len(v1)):

        v1[i] = (v1[i]*n)%p

    return v1


#Funcion que imprime los polinomios
def Imprimir(Im,p):
    """

    :param Im: El arreglo que representa el polinomio a imprimir
    :return: Una cadena que tiene el polinomio
    """

    Np = ""


    if len(Im)>=2:
        for l in range(len(Im)):

            if l == 0:
                if Im[l] != 0:
                    Np = f"+ {Im[l] % p}" + Np


            elif l == 1:
                if Im[l] != 0:
                    if Im[l] == 1:
                        Np = f"x^{l} + " + Np
                    else:
                        Np = f"{Im[l] % p}x  " + Np


            else:
                if Im[l] != 0:
                    if Im[l] == 1:
                        Np = f"x^{l} + " + Np
                    else:
                        Np = f"{Im[l] % p}x^{l} + " + Np

                elif res(Im) == 0:
                    Np = "0"


    else:
        contador = 0
        for l in range(len(Im)):

            if l == 0:
                if Im[l] != 0:
                    Np = f"{Im[l] % p}" + Np
                    contador = 1 + contador

            elif l == 1:
                if Im[l] != 0 and contador>0:
                    Np = f"{Im[l] % p}x + " + Np
                elif Im[l] != 0 and contador==0:
                    Np = f"{Im[l] % p}x  " + Np


    return Np


#Funcion que nos dice si un polinomio es reducible o irreducible
def Irreducible(p,pol,a):

    grad = math.floor( ( len(pol)/2) )+1

    g = list(map(list, product(a, repeat=grad)))

    #Suponemos que si es irreducible
    bandera = True



    for i in range(1,len(g)):
        if re(g[i])!=0:

            gp = FuncionMinimzar(g[i])

            c , r = Factorizacion(pol,gp,p)

            if res(r) == 0:
                # Es reducible
                bandera = False
                return bandera

    return bandera



# Función para invertir los elementos del polinomio a imprimir
def elementoCamp(a,pol):

    grad = len(pol)-1
    g = list(map(list, product(a, repeat =grad)))

    gn = []

    for i in range(len(g)):
        g[i].reverse()

    return g

#Función para multiplicar por un escalar a un polinomio
def multiplF(an,F):
    bn = []

    for i in range(len(an)):
        bn.append(F*an[i])

    return bn

#Funcion para dar los irreducibles que son solución de cada elemento del campo
def IrreduciblesCamp(polinomioG,p,pol,a ):

    """

    :param polinomioG: El polinomio de la extension de campos
    :param p: el primo del campo Zp
    :param pol: el polinomio al cual vamos a obtener su irreducible
    :param a: El campo Zp
    :return: el irreducible asociado al polinomio
    """

    grad = len(polinomioG)

    gn = list(map(list, product(a, repeat=grad)))
    # Vamos a verificar que el elemento al final es un multiplo del irreducible




    for i in range(1,len(gn)):
        a0 = []
        a1 = []
        an = []

        a0.append(gn[i][0])
        for j in range(1, grad):
            a0.append(0)

        for l in range(len(pol)):
            a1.append( (gn[i][1]*pol[l])%p )
            an.append(pol[l])



        sum = sumar(a0,a1,p)

        for k in range(2,grad):
            an = mult_polinom_Zp(an, pol, p)
            if gn[i][k] != 0 :
                bn = multiplF(an,gn[i][k])
                sum = sumar(bn,sum,p)


        if re(gn[i])<1:
            b = True

        else:
            gp = FuncionMinimzar(gn[i])
            b = Irreducible(p, gp, a)



        if res(sum) == 0 and b == True:

            return gn

        else:
            if len(sum) >= len(polinomioG) and re(sum) >= re(polinomioG) and b == True:

                c, r = Factorizacion(sum, polinomioG, p)
                if res(r) == 0:
                    bandera = False
                    return gn[i]


#Funcion que hace la division de dos polinomios
def Factorizacion(Np,Dp,p):

    """
    :param Np: El polinomio numerador
    :param Dp: El polinomio Denominador
    :param p: El p del campo Zp
    :return: El cociente y el residuo
    """

    loDp = len(Dp)-1
    pot = []
    coef = []


    b = re(Dp)

    g= re(Np)-b



    Dpc = (((Dp[b])**(p-2))%p)

    aux = list(Np)


    while g >= 0 and res(aux)!=0:

        pote = re(aux)-b
        #cof = Dpc * (((aux[re(aux)])**(p-2))%p)
        cof = (Dpc * aux[re(aux)])% p
        pot.append(pote)
        coef.append(cof)


        for j in range(loDp+1):

            aux[pote+loDp-j] = (aux[pote+loDp-j] - ((cof*Dp[loDp-j])%p)) %p

        g = re(aux) - b

    cociente = []
    for i in range(pot[0]+1):
        cociente.append(0)

    for i in range(len(coef)):

        cociente[pot[i]] = coef[i]


    return cociente,aux

#Función que regresa la mayor posición en el arreglo donde el numero es distinto de cero
def re(Np):

    """
    :param Np: Un polinomio en forma de arreglo
    :return: La mayor posicion en el arreglo en donde el numero es distinto de cero
    """

    for i in range(1,len(Np)):
        if Np[-i] != 0:
            return len(Np)-i

    return 0


#Función que regresa el elemento en la mayor posición en el arreglo donde el numero es distinto de cero
def re2(Np):

    """
    :param Np: Un polinomio en forma de arreglo
    :return: La mayor posicion en el arreglo en donde el numero es distinto de cero
    """

    for i in range(1,len(Np)):
        if Np[-i] != 0:
            return Np[-i]

    return 0


# Función que prueba que un polinomio no sea el polinomio 0
def res(Np):
    contador = 0
    for i in range(len(Np)):
        if Np[i] != 0:
            contador = 1+ contador

    return contador


def Normalizar(a,k,p):

    """
    :param a: El polinomio en forma de vector
    :param k: El número normalizador de maximo comun divisor
    :param p: El primo del campo Zp
    :return: El polinomio en forma de vector , ya normalizado
    """
    for i in range(len(a)):

        a[i] = (a[i]*k)%p
    return a


#Funcion que hace la suma de dos polinomios
def sumar(a,b,p):
    """

     :param a: El polinomio a en forma de vector a-b
     :param b: El polinomio b en forma de vector a-b
     :param p: El primo de campo Zp
     :return: la resta de los polinomios
    """


    if len(a) > len(b):

        resta = a.copy()

        for i in range(len(b)):

            a[i] = (a[i] + b[i]) %p

        return a

    else:

        for i in range(len(a)):
            b[i] = (a[i] + b[i]) % p

        return b

#Funcion que reduce el arreglo del polinomio hasta donde es diferente de cero
def FuncionMinimzar(pol):

    g = re(pol)

    ng = []

    for i in range(g+1):

        ng.append(pol[i])

    return ng


if __name__ == '__main__':

    # Se ingresará el polinomio de menor grado al mayor
    Np = [1,0,1] # Esto representa el polinomio x**2+1

    aux = Np.copy()
    # Se ingresará el primo del campo Zp
    p = 19

    a = []

    #Creamos una lista con los elementos en Zp
    for i in range(p):
        a.append(i)


    # Primero probamos que si sea irreducible
    b = Irreducible(p,Np,a)

    # Si es irreducible damos los elementos del campo
    if b==True:
        print("El polinomio es irreducible \n ")

        print("\n El polinomio " + Imprimir(Np,p) + f" es irreducible en Z_{p}[x]. El campo Z_{19}[x]/I , donde I = <" + Imprimir(Np,p) + ">, tiene 361 elementos: ")
        print("\n Sus elementos son los siguientes:  \n ")

        element =  elementoCamp(a,Np)

        for j in range(len(element)):

            polinom = Imprimir(element[j],p)

            if j < p:
                if j == 0:
                    print(f"El elemento_{j + 1} es : " + polinom + f" 0 + I tiene como polinomio irreducible: x ")

                else:
                    print(f"El elemento_{j + 1} es : " + polinom + f" + I tiene como polinomio irreducible: x + {j} ")

            else:
                irre = IrreduciblesCamp(Np,p,element[j],a)
                irre1 = Monico(irre,p)
                print(f"El elemento_{j + 1} es : " + polinom + f" + I tiene como polinomio irreducible: " + Imprimir(irre,p) )






        continua = True

    # Si no es no hacemos nada
    else:
        print("El polinomio es reducible ")
        continua = False




