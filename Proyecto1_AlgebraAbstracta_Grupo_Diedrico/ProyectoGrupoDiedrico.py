import itertools
from typing import List
import math


def producto(a: list, b1: list) -> list:
    """

    :param a: Es una lista de longitud n
    :param b1: Es una lista de longitud n
    :return: Una lista de la misma longitud
    """

    c = []
    for i in range(len(a)):

        c.append(b1[a[i]])

    return c

def inversa(a):

    """

    :param a: Es el elemento del cual queremos obtener su inversa
    :return: la inversa del elemento introducido
    """

    aux = [i for i in range(len(a))]
    j = 0



    for i in a:
        aux[i] = j
        j = j +1


    return aux

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


def GrupoDie(n):

    """
    :param n: Es el orden del grupo /2
    :return: El grupo diédrico
    """
    a = []
    r = []
    s = []
    m = []
    mb = {}
    mbo = {}


    # Creamos la identidad
    for i in range(n):
        a.append(i)

    # Creamos a r
    for i in range(n):
        r.append(a[i - 1])

    aux = list(r)

    m.append(a)
    mb["1"] = a
    mbo[tuple(a)] = "1"

    # Creamos a S
    for i in range(1,n+1):
        s.append(a[-i])

    print(s)


    # Creamos todos los elementos de r

    for i in range(len(aux) - 1):
        m.append(r)

        mb[f"r^{i+1}"] = r
        mbo[tuple(r)] = f"r^{i+1}"
        r = producto(aux, r)



    # Agregamos a s,sr^1, sr^2,....,sr^n-1 en la lista

    for i in range(len(aux)):

        mb[f"s*r^{i}"] = producto(s,m[i])
        mbo[tuple(producto(s,m[i]))] = f"s*r^{i}"
        m.append(producto(s,m[i]))


    return m, mb, mbo

def RegresarInv(Grup,GrupI):

    """
    :param Grup: Es el grupo Diédrico
    :param GrupI: Es el grupo Diédrico en forma de diccionario
    :return: La inversa en orden del Grupo Diedrico en forma de lista y diccionario
    """

    # Creamos la lista de inversos

    GrupInv = []
    GrupInvB = {}
    GrupInveB = {}


    #for i in Grup
    for i in Grup:
        GrupInv.append(inversa(i))
        GrupInvB[tuple(inversa(i))] = GrupI[tuple(inversa(i))]
        GrupInveB[GrupI[tuple(inversa(i))]] = tuple(inversa(i))





    return GrupInv, GrupInvB, GrupInveB

def RegresarOrden(Grup1):
    """
    :param Grup1: Introducimos el elemento a sacar el orden
    :return: Regresa el orden del elemento
    """

    GrupOrden = []

    for i in Grup1:
        GrupOrden.append(order(i))

    return GrupOrden

#Encuentra los sugrupos
def Subgrupos(G,Gb,n):
  """

  :param G: Es el Grupo Diédrico
  :param Gb: Es el Grupo Diédrico en forma de diccionario
  :param n: Es el número de lugares en donde se van a combinar los elementos del Grupo Diédrico
  :return: Todos los subgrupos de orden n
  """


  #Encontramos todas las posibles permutaciones de orden div
  Combinaciones = list(itertools.combinations(G,n))
  Combinaciones1 = list(itertools.combinations(Gb,n))
  SubG = []
  SubGB = []




  for i in Combinaciones:


      SiG=True

      #Para cada elemento del subgrupo
      for j in i:
      #Se tiene que operar con cada uno de los elementos y cumplir la cerradura
          for k in i:
              El = producto(j, k)

              #Encontramos al menos una operacion que no este

              if El not in i:
                  SiG = False
                  break


      if(SiG == True):
          SubG.append(i)
          SubGB.append(Combinaciones1[Combinaciones.index(i)])

  return SubG, SubGB


def Normal(GrupDied, Inv , Subgrup ,SubGB):

    """
    :param GrupDied: Es el Grupo Diédrico
    :param Inv: Es la lista de los inversos del Grupo Diédrico
    :param Subgrup: Son todos los Subgrupos de cierto orden k
    :param SubGB: Son todos los Subgrupos de cierto orden en forma de diccionario
    :return: Todos los Subgrupos normales de orden k
    """

    SubNormados = []
    SubPrueba = []

    #Tomamos cada Subgrupo
    for k in range(len(Subgrup)):
        #Suponemos que es normal
        Bandera = True
        #Tomamos los elementos del subgrupo elegido anteriormente
        for i in range(len(Subgrup[k])):
            # Tomamos cada elemento del grupo con su inverso y realizamos la operacion
            #g*h*g^-1 para comprobar que sea normal
            for j in range(len(GrupDied)):

                #Verificamos que si este en el subgrupo
                if producto(GrupDied[j], producto(Subgrup[k][i], Inv[j])) not in Subgrup[k]:
                    #Si encontramos al menos operacion que no este entonces no es normal
                    Bandera = False
                    break

        if Bandera == True:

            SubNormados.append(Subgrup[k])
            SubPrueba.append(SubGB[k])


    return SubNormados,SubPrueba


n = int(input("Introduce el elemento a obtener "))


Grupo, GrupoBiblioteca, Gbp = GrupoDie(n)

GrupoOrden = RegresarOrden(Grupo)
print(f"Este es el grupo de grupo Diedrico de orden {2*n}\n ")
print(GrupoBiblioteca)



print("\n Esta es la lista inversa en orden: \n")
GrupoInverso,GrupoBibliotecaInverso, GBI = RegresarInv(Grupo,Gbp)

print(GBI)

print("\n Este es el orden: \n")
print(GrupoOrden)

print("\n El grupo de orden 1 es: [0,1,2,3,4] \n")
print(f"El grupo de orden {2*n} es: {GrupoBiblioteca} \n")



for i in range(2,len(Grupo)):
    if len(Grupo) % i == 0:
        print(f"\n Estos son todos los subgrupos de orden {i} en D{2*n} son: \n  ")
        Sub, SubB = Subgrupos(Grupo,GrupoBiblioteca,i)
        print(Sub)
        print(SubB)

        print(f"\n Estos subgrupos son normales de orden {i} en D{2*n} \n ")
        SubN, SubNP = Normal(Grupo, GrupoInverso,Sub,SubB)
        print(SubN)
        print(SubNP)
















