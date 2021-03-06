###################################
import re
from functools import reduce
import json

# Expresiones Regulares

#Ejercicio 1
def verificadorMatricula(matricula):

    validador = re.compile('^(L[VQ]-[A-Z]{2}([D-Z]{1}|[A-B]{1}))|(LV-[XS][0-9]{3})|(LV-(SX)[0-9]{3}$)')
    matriculaAceptada = validador.match(matricula)

    if (matriculaAceptada):
        return print("matricula ingresada es correcta")
    else:
        return print("matricula ingresada es incorrecta")


verificadorMatricula(input('ingrese matricula a validar, recuerde comenzar por las letras LV o LQ en mayusculas '))

#Ejercicio 2

def verificadorNumero(numero):

    comparador = re.compile('^[0-1]?[0-8]?[0-9]{1,2}$')
    numeroAceptado = comparador.match(numero)

    if (numeroAceptado):
        return print("correcto es un numero Natural inferior a 1900")
    else:
        return print("ingreso un numero incorrecto")


verificadorNumero(input('ingrese un numero natural inferior a 1900 '))


#Ejercicio Extra

def verificadorCadena(cadena):

    analizador = re.compile('[A-Z][a-z]+')
    cadenaMatch = analizador.match(cadena)

    if (cadenaMatch):
        return print(f"'{cadenaMatch.group()}' es la primera palabra de la cadena con letra inicial Mayuscula y resto en minuscula")
    else:
        return print("cadena no tiene expresion de coicidencia")


verificadorCadena(input('ingrese cadena de caracteres  '))

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
        return ele1 == ele2 and listas_iguales(l1, l2)
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



# Colecciones

# Ejercicio 2

def generarLista(n):
    if n == 0:
        return [0]
    else:
        lista = generarLista(n- 1)
        lista.append(n)
        return lista

def generarPI(n):
    lista=generarLista(n)
    terminos = list(map(lambda x: ((4 * ((-1) ** x)) / ((2 * x) + 1)),lista))
    suma= reduce(lambda x,y: x + y, terminos)
    return suma

print(generarPI(int(input('ingresar el valor de elementos de a sumar en la Serie de Leibniz  '))))

# Formato de Intercambio de Datos  ##############################################

import json


docSensores_json= '''
[
{"nombre": "estacion01",
 "temperatura": {"valor": 25,"unidad":"??C"},
 "presion": {"valor": 1,"unidad":"atm"},
 "humedad": {"valor":35,"unidad":"%"},
 "velociViento": {"valor":10,"unidad":"km/h"},
 "direccionViento": {"coordenada":"Norte"},
 "bateria": {"unidad":"mV",
             "mediciones": [0.5,0.4,0.6,0.8,0.35,0.45,0.18,0.54,0.55,0.6,0.48,0.22,0.15,0.30,0.70,0.43,0.44,0.25]}
},
{"nombre": "estacion02",
 "temperatura": {"valor": 68,"unidad":"??F"},
 "humedad": {"valor":50,"unidad":"%"},
 "bateria": {"unidad":"mV",
             "mediciones": [0.1,0.2,0.5,0.45,0.55,0.25,0.28,0.34,0.45,0.62,0.29,0.31,0.25,0.35,0.75,0.33,0.44,0.25]}
},
{"nombre": "estacion03",
 "temperatura": {"valor": 30,"unidad":"??C"},
 "presion": {"valor": 1.01,"unidad":"atm"},
 "humedad": {"valor":40,"unidad":"%"},
 "bateria": {"unidad":"mV",
             "mediciones": [0.25,0.14,0.46,0.18,0.15,0.75,0.48,0.34,0.55,0.62,0.38,0.52,0.35,0.28,0.20,0.43,0.44,0.25]}
}
]
'''


#Ejercicio1


Lista_diccs= json.loads(docSensores_json)

ListaMed=[]
sumatroria=0
nombre="estacion03"
if (nombre=="estacion01"):
    print(f" La Estaci??n01 tiene:'{len(Lista_diccs[0])-2}' sensores")
    print(f" Temperatura :" "{} {}".format(Lista_diccs[0]["temperatura"]["valor"],Lista_diccs[0]["temperatura"]["unidad"]))
    print(f" Presion:" "{} {}".format(Lista_diccs[0]["presion"]["valor"],Lista_diccs[0]["presion"]["unidad"]))
    print(f" humedad:" "{} {}".format(Lista_diccs[0]["humedad"]["valor"], Lista_diccs[0]["humedad"]["unidad"]))
    print(f" velocidad viento:" "{} {}".format(Lista_diccs[0]["velociViento"]["valor"], Lista_diccs[0]["velociViento"]["unidad"]))
    print(f" direcci??n del viento:" "{}".format(Lista_diccs[0]["direccionViento"]["coordenada"],))

else:
         if (nombre=="estacion02"):
             print(f" La Estaci??n01 tiene:'{len(Lista_diccs[1]) - 2}' sensores")
             print(f" Temperatura :" "{} {}".format(Lista_diccs[1]["temperatura"]["valor"],Lista_diccs[1]["temperatura"]["unidad"]))
             print(f" humedad:" "{} {}".format(Lista_diccs[1]["humedad"]["valor"], Lista_diccs[1]["humedad"]["unidad"]))
         else:
              if (nombre=="estacion03"):
                 print(f" La Estaci??n01 tiene:'{len(Lista_diccs[2]) - 2}' sensores")
                 print(f" Temperatura :" "{} {}".format(Lista_diccs[2]["temperatura"]["valor"],Lista_diccs[2]["temperatura"]["unidad"]))
                 print(f" Presion:" "{} {}".format(Lista_diccs[2]["presion"]["valor"], Lista_diccs[2]["presion"]["unidad"]))
                 print(f" humedad:" "{} {}".format(Lista_diccs[2]["humedad"]["valor"], Lista_diccs[2]["humedad"]["unidad"]))
              else:
                 print('nombre de estaci??n errado')



#Ejercicio2




