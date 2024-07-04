import math

def unidades(n):
    '''
    :param n: Es un natural mayor o igual a 2
    :return: Las unidades de Z_n , es decir son los elementos de Z_n que son invertibles con respecto
    al producto
    '''
    units = []
    for i in range(1,n):
        if math.gcd(i,n) == 1:
            units.append(i)

    return units

def orden(a,n):
    '''

    :param a: Es un elemento de las unidades
    :param n: un entero mayor o igual a 2
    :return: El natural i más pequeño tal que a**i es igual a 1
    '''

    for i in range(1,n):
        if (a**i-1)% n == 0:
            return i

def generadores(n):
    '''

    :param n: Es el grupo a obtener el grupo generado
    :return: el grupo generado aditivamente
    '''
    units = unidades(n)
    print(units)
    for unidad in units:
        print(f"La unidad es {unidad}")
        generado_unidad =  [(unidad**k % n) for k in range(n)]
        generado_unidadSet = set ( [(unidad**k % n) for k in range(n)])
        print(generado_unidad)
        print(generado_unidadSet)



#Ahora encontrar el generador de U(n)
n = int(input("Introduce un entero: "))

g = unidades(n)
print(g)
print(generadores(n))

ordenes = []

for j in g:
    ordenes.append(orden(j,n))
print(ordenes)
print("Notemos que los generadores son las raices primitivas, pero solo se pueden generar con los numeros primos")
