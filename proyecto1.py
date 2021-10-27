###################################
# Funciones de recursion

#Ejercicio 1
def codificar(num):
    if num < 10:
        if num % 2 == 0:
            return 1
        else:
            return 2
    else:
        if num % 2 == 0:
            return (codificar(int(num / 10)) * 10 + 1)
        else:
            return (codificar(int(num / 10)) * 10 + 2)

#Ejercicio 2
#Convertir una lista de listas de enteros en una sola.
def listar(lista) :
    if len(lista) != 0 :
        elemento = lista[len(lista)-1]
        lista.pop()
        miLis = listar(lista)
        miLis += elemento
        return(miLis)
    else:
        l = list()
        return(l)

#Ejercicio 3
#Decidir si dos listes de enteros son iguales.
def listas_iguales(l1, l2):
    if len(l1) != len(l2):
        return False
    elif len(l1) != 0:
        ele1 = l1.pop()
        ele2 = l2.pop()
        if ele1 == ele2 and listas_iguales(l1, l2):
            return True
        else:
            return False
    else:
        return True

#Ejercicio 4
# susesion de restas para dividir A / B
def division_entera(A, B):
    if A < B:
        return 0
    else:
        return (division_entera(A - B, B) + 1)

#Ejercicio propuesto 1
# Dado un numero entero devolver verdadero si tiene cantidad de digitos par y falso si tiene cantidad de digitos impar.
# ej: 105 devuelve falso porque tiene 3
# 6789 devuelve verdadero porqie tiene 4
def esPar(num):
    if num == 0:
        return False
    else:
        if esPar(num / 10):
            return False
        else:
            return True

#Ejercicio propuesto 2
# a partir de un numero entero generar otro con un numero 2 en la posicion do de halla digitos en posicion par.
#ej: para 123456
# genera 123252
def un_dos(num):
        if num== 0 :
            return 0
        else :
            miNum = un_dos(int(num/10))
            ultimo = num %10
            if (esPar(num)):
                miNum = 2+miNum*10
            else:
                miNum = ultimo+miNum*10
            return miNum

#Ejercicio Propuesto 3
# Dada una lista de patentes de automoviles generar otra lista con todas las patentes que comiencen con AA.
def lista_AA(lista):
    if len(lista) == 0:
        lista = []
        return lista
    else:
        elem = lista.pop()
        listaAA = lista_AA(lista)
        if "AA" in elem[0:2]:
            listaAA.append(elem)
        return listaAA



# def listar(elem):
#     if len(elem) == 0:
#         lista = list()
#         return lista
#     else:
#         lista = listar(elem.pop()))
#     if esEntero(lista[0]) :
#         elemento.append(elem)
#         return elemento
#     else :
#         lista = listar(elem.pop())

