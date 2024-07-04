import numpy as np


def Imprimir(Im):
    """

    :param Im: El arreglo que representa el polinomio a imprimir
    :return: Una cadena que tiene el polinomio
    """

    Np = ""


    if len(Im)>2:
        for l in range(len(Im)):

            if l == 0:
                if Im[l] != 0:
                    Np = f"+ {Im[l] % p}" + Np

            elif l == 1:
                if Im[l] != 0:
                    Np = f"{Im[l] % p}x  " + Np

            else:
                if Im[l] != 0:
                    Np = f"{Im[l] % p}x^{l} + " + Np

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


    while g >= 0 and res(aux) != 0:

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

def mcd(Np,Dp,p):

    """

    :param Np: El polinomio numerador
    :param Dp: El polinomio Denominador
    :param p: El primo del campo Zp
    :return: El maximo comun divisor
    """


    AuxDp = list(Dp)
    residuos = []
    cocientes = []

    cociente, residuo = Factorizacion(Np,Dp,p)
    cocientes.append(cociente)

    resd = []
    for i in range(re(residuo)+1):
        resd.append(residuo[i])

    residuos.append(resd)


    while res(resd)>0:



        AuxNp = AuxDp
        AuxDp = resd

        cociente, residuo = Factorizacion(AuxNp, AuxDp, p)
        cocientes.append(cociente)
        resd = []
        for i in range(re(residuo) + 1):
            resd.append(residuo[i])

        residuos.append(resd)

    return residuos,cocientes


def re(Np):

    """

    :param Np: Un polinomio en forma de arreglo
    :return: La mayor posicion en el arreglo en donde el numero es distinto de cero
    """

    for i in range(1,len(Np)):
        if Np[-i] != 0:
            return len(Np)-i

    return 0

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

def Bezut(resid, cocien,p):
    """

    :param resid: El vector de todos los residuos
    :param cocien: El cociente
    :param p: El primo en el campo Zp
    :return: Los coeficientes de Bezut
    """

    u0 = [1]
    u1 = [0]
    v0 = [0]
    v1 = [1]

    for i in range(len(cocien)):

        q1 = np.array(cocien[i])
        un = np.array(u1)
        producto = np.convolve(q1,un)% p
        producto2 = np.convolve(q1,np.array(v1))%p

        u = restar(u0,producto,p)
        v = restar(v0,producto2,p)

        u0 = u1
        u1 = u
        v0 = v1
        v1 = v

    u0 = Normalizar(u0,resid,p)
    v0 = Normalizar(v0,resid, p)

    return u0 , v0



def restar(a,b,p):
    """

     :param a: El polinomio a en forma de vector a-b
     :param b: El polinomio b en forma de vector a-b
     :param p: El primo de campo Zp
     :return: la resta de los polinomios
    """




    if len(a) > len(b):

        resta = a.copy()

        for i in range(len(b)):

            a[i] = (a[i] - b[i]) %p

        return a

    else:
        for k in range(len(b)):
            b[k] = (b[k]*(-1))%p

        for i in range(len(a)):
            b[i] = (a[i] + b[i]) % p

        return b




if __name__ == '__main__':


    Np = [2, 3, 1, 1, 2]
    aux = Np.copy()
    Dp = [2, 2, 1, 1,1]

    if len(Np) < len(Dp):
        print("El divisor es mas grande que el dividendo por lo tanto se van  cambiar: ")
        Np = Dp
        Dp = aux.copy()


    p = 5

    Cocien, Res = Factorizacion(Np,Dp,p)

    print(f"El dividendo es: {Imprimir(Np)}")
    print(f"El divisor es: {Imprimir(Dp)}")


    print(f"El cociente es {Cocien} : {Imprimir(Cocien)} \n")

    print(f"El residuo es {Res} : {Imprimir(Res)} \n")


    r,c = mcd(Np,Dp,p)

    if len(r)>1:
        re = r[-2]


    else:
        re = r[-1]




    k1 = (re[-1]**(p-2))%p

    re = Normalizar(re,k1,p)
    u,v = Bezut(k1,c,p)

    print(f"El maximo comun divisor es {re}:" + Imprimir(re))

    # u es para el numerador y el v para en denominador
    print("Los coeficientes de Bezut son: " + Imprimir(u) + "  y  " + Imprimir(v))

    print("Comprobación de los coeficientes de Bezut: ( (" + Imprimir(u) + ") * ("+Imprimir(Np) +") )" + " + " + "( (" +Imprimir(v) + ") * (" + Imprimir(Dp) + ") )" + " = " + Imprimir(re) )












