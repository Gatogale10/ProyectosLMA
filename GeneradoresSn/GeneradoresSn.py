import itertools
import numpy as np



def PermCiclos(n):
    a = []

    #Creamos la identidad
    a = np.arange(n)
    print(a)

    #Creamos todas las permutaciones
    Permutaciones = list(itertools.permutations(a, n))

    #Lista de los ciclos
    ciclosA = []

    #Lista de las transposiciones
    Trp2 = []

    #Lista de las permutaciones pares
    GrupoAlternante = []



    # Obtenemos el ciclo de todas las permutaciones
    for i in Permutaciones:
        #Son los ciclos de una permutación dada
        perm = []
        # Trasposiciones asociadas a la permutación
        Trp = []

        #Guardamos los valores que ya hicimos para no repetir en los ciclos
        Ver = []


        for j in range(len(i)):
            aux = []
            m = j

            #Verificamos que no es una orbita con un elemento
            if m != i[m] and m not in Ver:

                #Se para el programa cuando el elemento se repite , ya se vuelve un ciclo
                while m not in aux:

                    aux.append(m)
                    m = i[m]
                    Ver.append(m)

                perm.append(aux)

                #Transpocion del ciclo dado
                if len(aux) == 2:
                    Trp.append(aux)

                #Formula si la cardinalidad del ciclo es mayor que 2
                else:

                    for d in range(len(aux)-1):
                        aux2 = []
                        aux2.append(aux[0])
                        r = aux[len(aux)-1-d]
                        aux2.append(r)
                        Trp.append(aux2)


        #Vemos si la permutacion es par o impar
        if len(Trp)%2 == 0:
            paridad = "Par"
            GrupoAlternante.append(i)

        else:
            paridad = "Impar "

        #Imprimimos la permutación, el ciclo, las Transposiciones , la paridad, las Factorizaciones
        print(f"Permutacion  : {i}         Ciclo :  {perm}              Transposiciones:     {Trp}             Paridad: {paridad}    Factorizacion : {factorizacion(Trp)} \n")

        Trp2.append(Trp)

        ciclosA.append(perm)

    #Imprimimos el grupo alternante
    print(f"Grupo Alternante {GrupoAlternante}")
    print(len(GrupoAlternante))
    return Permutaciones, ciclosA , Trp2



def factorizacion(T):

    '''

    :param T: Las transposiciones
    :return: La factorización

    '''


    cadenaGeneral = ""


    # Caso trivial
    if len(T) == 0:

        cadenaGeneral = cadenaGeneral + "vació, es la trivial"



    else:

        # Vamos transposición por transposición
        for i in T:
            cade = ""

            # Obtenemos la distancia entre los dos datos
            d = i[1] - i[0]


            if d == 1:

                if i == [0,1]:
                    cadenaGeneral = cadenaGeneral + "s"

                elif i == [1,2]:
                    cadenaGeneral = cadenaGeneral + f"rsr^{-i[0]}"

                else:
                    cadenaGeneral = cadenaGeneral + f"r^{i[0]}sr^{-i[0]}"


            # Usamos la formula recursiva para obtener todos los elementos
            else:

                if [i[0],i[0]+1] == [0,1]:
                    cade = cade + "s"

                elif i == [1,2]:
                    cadenaGeneral = cadenaGeneral + f"rsr^{-i[0]}"

                else:
                    cade = cade + f"r^{i[0]}sr^{-i[0]}"

                cadenaGeneral = cadenaGeneral + cade + Recursividad([i[0]+1,i[1]]) + cade

    return cadenaGeneral


def Recursividad(Td):


    cadenaGeneral = " "
    cade = ""

    d = Td[1]-Td[0]

    if d == 1:

        if Td == [0, 1]:
            cadenaGeneral = cadenaGeneral + "s"

        elif Td == [1, 2]:
            cadenaGeneral = cadenaGeneral + f"rsr^{-Td[0]}"

        else:
            cadenaGeneral = cadenaGeneral + f"r^{Td[0]}sr^{-Td[0]}"

    else:
        if [Td[0], Td[0] + 1] == [0, 1]:
            cade = cade + "s"

        elif [Td[0], Td[0] + 1] == [1, 2]:
            cade = cade + f"rsr^{-Td[0]}"

        else:
            cade = cade + f"r^{Td[0]}sr^{-Td[0]}"

        cadenaGeneral = cade + Recursividad([Td[0]+1,Td[1]]) + cade


    return cadenaGeneral




P, C, T = PermCiclos(8)

















