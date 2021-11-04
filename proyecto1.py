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
        return True
    else:
        return False


#verificadorMatricula(input('ingrese matricula a validar, recuerde comenzar por las letras LV o LQ en mayusculas '))

#Ejercicio 2

def verificadorNumero(numero):

    comparador = re.compile('^[0-1]?[0-8]?[0-9]{1,2}$')
    numeroAceptado = comparador.match(numero)

    if (numeroAceptado):
        return True
    else:
        return False


#verificadorNumero(input('ingrese un numero natural inferior a 1900 '))


#Ejercicio Extra

def verificadorCadena(cadena):

    analizador = re.compile('[A-Z][a-z]+')
    cadenaMatch = analizador.match(cadena)

    if (cadenaMatch):
        return print(f"'{cadenaMatch.group()}' es la primera palabra de la cadena con letra inicial Mayuscula y resto en minuscula")
    else:
        return print("cadena no tiene expresion de coicidencia")


#verificadorCadena(input('ingrese cadena de caracteres  '))

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

#print(generarPI(int(input('ingresar el valor de elementos de a sumar en la Serie de Leibniz  '))))

# Formato de Intercambio de Datos  ##############################################


docSensores_json= '''
[  
{"nombre": "estacion01",
 "temperatura": {"valor": 25,"unidad":"°C"},
 "presion": {"valor": 1,"unidad":"atm"},
 "humedad": {"valor":35,"unidad":"%"},
 "velociViento": {"valor":10,"unidad":"km/h"},
 "direccionViento": {"coordenada":"Norte"},
 "bateria": {"unidad":"mV",
             "mediciones": [0.50,0.40,0.60,0.80,0.35,0.45,0.18,0.54,0.55,0.60,0.48,0.22,0.15,0.30,0.70,0.43,0.44,0.25,0.30,0.42]}
},
{"nombre": "estacion02",
 "temperatura": {"valor": 68,"unidad":"°F"},
 "humedad": {"valor":50,"unidad":"%"},
 "bateria": {"unidad":"mV",
             "mediciones": [0.10,0.20,0.50,0.45,0.55,0.25,0.28,0.34,0.45,0.62,0.29,0.31,0.25,0.35,0.75,0.33,0.44,0.25,0.55,0.36]}
},
{"nombre": "estacion03",
 "temperatura": {"valor": 30,"unidad":"°C"},
 "presion": {"valor": 1.01,"unidad":"atm"},
 "humedad": {"valor":40,"unidad":"%"},
 "bateria": {"unidad":"mV",
             "mediciones": [0.25,0.14,0.46,0.18,0.15,0.75,0.48,0.34,0.55,0.62,0.38,0.52,0.35,0.28,0.20,0.43,0.44,0.25,0.19,0.32]}
}
]
'''

# Ejercicio 1
def imprimirSensoresEstacion(estacion):
    print("Cantidad de sensores de la estacion "'"{}"'" : {}".format(estacion['nombre'],len(estacion)-2))
    for key in estacion:
        sensor = estacion[key]
        if key != 'nombre' and key != 'bateria' and key != 'direccionViento':
            print(key + ": {} {}" .format(sensor.get('valor'),sensor.get('unidad')))
        elif key == 'direccionViento' :
            print(key + ": {}".format(sensor.get('coordenada')))





#Ejercicio2

Lista_diccs= json.loads(docSensores_json)


def generarPromedios(lista):
    promVolts = []
    for elemento in lista:
        suma=0
        medidas=(elemento.get("bateria").get("mediciones"))
        for medida in medidas:
           suma+=medida
        promedio=suma/(len(medidas))
        promVolts.append(promedio)
    return promVolts

def encontrarMenor(listaVolt):
    menor=1000
    pos=0
    for volt in listaVolt:
        if (volt<menor):
            menor=volt
            posicion=pos
        pos+=1
    return posicion


def estacionValida(nombre, lista_diccs):
    esta = False
    for estacion in lista_diccs:
        if estacion.get('nombre') == nombre:
            esta = True
    # print(esta)
    return esta


def obtenerPosEstacion(nombre, lista_estaciones):
    pos = 0
    estacion = lista_estaciones[pos]
    while not nombre == estacion['nombre'] and pos < len(lista_estaciones):
        estacion = lista_estaciones[pos]
        pos = pos + 1

    if pos == len(lista_estaciones):
        return -1
    else:
        return pos


##################################################
# menu de navegacion de programa                ##
##################################################
salir = False
print("Bienvenido al programa de Wehitt-Salazar\n")

while not salir :
    print("Seleccione una opcion numerica del menu:\n")

    print(" - 1- Validar Matriculas de aeronaves")
    print(" - 2- Validar cadenas de numeros naturales")
    print(" - 3- Validacion de una cadena")
    print(" - 4- Codificar numero entero")
    print(" - 5- Convertir una lista de listas en una sola lista")
    print(" - 6- Decidir si dos listas de numeros enteros son iguales")
    print(" - 7- Division entera de dos enteros positivos.")
    print(" - 8- Decidir si un numero entero tiene cantidad de digitos par")
    print(" - 9- Codificar entero con un 2 en cada posicion par.")
    print(" -10- Filtrar pantentes AA de una lista de patentes")
    print(" -11- Map filter y reduce")
    print(" -12- Aproximacion de numero PI")
    print(" -13- Mostrar sensores disponibles")
    print(" -14- Mostrar estacion con menos bateria")
    #print(" -15- Mostrar estacion con menos bateria 2")
    print(" -15- Salir")
    print("")
    opcion = int(input("Ingrese la opcion: "))


    listoMatricula = False
    listoCadenaNaturales = False
    listoCadenaExtra = False
    listoCodificarNumero = False
    listoListaDeListas = False
    listoListasIguales = False
    listoDivisionEntera = False
    listoCantidadDigitosPar = False
    listoUnDosEnCadaPosPar = False
    listoFiltrarPatentes = False
    listoAproximarPI = False
    listoEstacionSensores = False
    if opcion == 1 :
        print("\nLas matriculas de las aeronaves en Argentina tienen un formato de acuerdo a su tipo. Comienzan con LV o con LQ")
        while not listoMatricula :
            print("\nAlgunos ejemplos de matriculas son: LV-QWE LQ-ABE LV-X443 LV-S586 LV-SX334.")
            matricula = input("Ingrese la matricula a validar se utilizara esta expresion: ""^(L[VQ]-[A-Z]{2}([D-Z]{1}|[A-B]{1}))|(LV-[XS][0-9]{3})|(LV-(SX)[0-9]{3}$)"" \n")
            if verificadorMatricula(matricula) :
                print("La matricula fue ingresada correctamente.")
            else :
                print("La matricula no fue ingresada correctamente.")
            opcionMatricula = input("Desea ingresar otra matricula? s/n ")
            listoMatricula = opcionMatricula == 'n'
    elif opcion == 2 :
        print("\nSe validara la cadena de numeros naturales menores a 1900")
        while not listoCadenaNaturales :
            cadena = input("\nIngrese cadena de numeros naturales: ")
            if verificadorNumero(cadena) :
                print("La cadena tiene un formato correcto.")
            else :
                print("La cadena no tiene un formato correcto.")
            opcionCadenaNumeros = input("Desea ingresar otra cadena? s/n")
            listoCadenaNaturales = opcionCadenaNumeros == 'n'
    elif opcion == 3 :
        print("Se analizara si la cadena ingresada contiene la primer letra de la primer palabra en mayuscula y las demas letras en minuscula.")
        while not listoCadenaExtra :
            cadena = input("Ingrese la cadena se evaluara la expresion [A-Z][a-z]+: ")
            verificadorCadena(cadena)
            opcionCadena = input("Desea ingresar otra cadena? s/n ")
            listoCadenaExtra = opcionCadena == 'n'
    elif opcion == 4 :
        print("Se codificara un numero entero. Cada digito par se modificara por un 1 y cada digito impar se modificara por un 2.")
        while not listoCodificarNumero :
            numero = int(input("Ingrese numero entero: "))
            print("El numero "+ str(numero) +" se codifica a "+ str(codificar(numero)) )
            opcionCodificar = input("Desea ingresar otro numero? s/n ")
            listoCodificarNumero = opcionCodificar == 'n'
    elif opcion == 5 :
        while not listoListaDeListas :
            print("Se procedera a generar una lista de listas de enteros")
            lista = []
            listoGenerarLista = False
            while not listoGenerarLista :
                cadena = input("Ingrese enteros separados por "","" : ")
                lista.append(cadena.split(','))
                opcion = input("Desea agregar otra lista de enteros? s/n ")
                listoGenerarLista = opcion == 'n'
            print("Ha generado la sigueiente lista: ")
            print(lista)
            print("La lista resultante es: ")
            print(listar(lista))
            opcion = input("Desea generar otra lista? s/n ")
            listoListaDeListas = opcion == 'n'
    elif opcion == 6 :
        while not listoListasIguales :
            print("Se procedera a generar las listas para decidir si son iguales.")
            lista1 = []
            lista2 = []
            cadenaLista1 = input("Ingrese los numeros enteros separados por "","" para la primera lista:")
            cadenaLista2 = input("Ingrese los numeros enteros separados por "","" para la segunda lista:")
            lista1.append(cadenaLista1.split(','))
            lista2.append(cadenaLista2.split(','))
            if listas_iguales(lista1,lista2) :
                print("Las listas ingresadas son iguales")
            else :
                print("Las listas ingresadas no son iguales")
            opcion = input("Desea ingresar las listas nuevamente? s/n ")
            listoListasIguales = opcion == 'n'
    elif opcion == 7 :
        while not listoDivisionEntera :
            print("Se procedera a computar la division entera de dos numeros enteros.")
            numerador = int(input("Ingrese el numerador: "))
            denominador = int(input("Ingrese el denominador, este debe ser distinto de 0: "))
            print("El resultado de la division entera de "+str(numerador)+"/"+str(denominador)+" es: ")
            print(division_entera(numerador,denominador))
            opcion = input("Desea volver a operar? s/n ")
            listoDivisionEntera = opcion == 'n'
    elif opcion == 8:
        while not listoCantidadDigitosPar :
            print("Se computara si un numero entero tiene cantidad de digitos par o no \n"+
                  "ej: 105 devuelve falso porque tiene 3 digitos \n" +
                  "    6789 devuelve verdadero porque tiene 4 digitos\n"
                  )
            numero = int(input("Ingrese numero entero: "))
            if esPar(numero) :
                print("El numero ingresado tiene cantidad de digitos par")
            else :
                print("El numero ingresado tiene cantidad de digitos impar")
            opcion = input("Desea volver a operar? s/n ")
            listoCantidadDigitosPar = opcion == 'n'
    elif opcion == 9 :
        while not listoUnDosEnCadaPosPar :
            print("Se generara un numero a partir del que usted ingrese con un numero 2 en la posicion donde halla digitos en posicion par.\n"+
                    " ej: para 123456\n"+
                    "  genera 123252\n")
            numero = int(input("Ingrese numero para operarlo: "))
            numero2 = un_dos(numero)
            print("El numero generado es: "+str(numero2))
            opcion = input("Desea volver a operar? s/n ")
            listoUnDosEnCadaPosPar = opcion == 'n'
    elif opcion == 10 :
        while not listoFiltrarPatentes :
            print("Se filtraran las patentes de una lista que se generara a continuacion.")
            print("El formato de las patentes debe ser XX-ddd-XX. donde X es una letra en mayuscula, y d es un digito")
            lista = []
            listoGenerarLista = False
            while not listoGenerarLista:
                cadena = input("Ingrese patente: ")
                lista.append(cadena)
                opcion = input("Desea agregar otra patente? s/n ")
                listoGenerarLista = opcion == 'n'
            print("Ha generado la sigueiente lista: ")
            print(lista)
            print("Y se han filtrado: "+str(lista_AA(lista)))
            opcion = input("Desea volver a operar? s/n ")
            listoFiltrarPatentes = opcion == 'n'
    elif opcion == 11 :
        print("Las funciones map() filter() y reduce() son funciones que se aplican a listas de elementos.\n"+
              "Estas son practicas para manipular listas sin tener que llegar a escribir estructuras de repeticion.\n"+
              "Por ejemplo map(una_funcion, una_lista) en Python aplica una función a cada uno de los elementos de una lista y la retorna.\n"+
              "La funcion filter(una_funcion, una_lista) filtra y retorna una lista de elementos para los que una función devuelve True.\n" +
              "La funcion reduce(una_funcion, valores) se utiliza principalmente para llevar a cabo un cálculo acumulativo sobre una lista de valores y devolver el resultado.\n")
        print("\n")
        print("Para entender mejor estas funciones vea el archivo .jpg que se adjunta junto a este programa.\n")
        input("Presione ENTER para volver al menu.")
    elif opcion == 12 :
        print("El numero PI es un numero irracional y una de las constantes matemáticas más importantes.\n"+
              "Como no es posible determinar su valor exacto, se puede aproximar mediante la serie de Leibniz.\n" +
              "Una aproximacion puede ser: 3.1425956623646125\n")
        while not listoAproximarPI :
            numero = int(input("Ingrese un numero natural para computar en la serie (menor a 997): "))
            print("Usted aproximo el numero PI a :" + str(generarPI(numero)))
            opcion = input("Desea volver a intentarlo? s/n ")
            listoAproximarPI = opcion == 'n'
    elif opcion == 13 :
        print("A partir del nombre de la estacion se mostrara en pantalla los sensores disponibles.\n" +
              "Por ejemplo: estacion01")
        while not listoEstacionSensores :
            nombre = input("Ingrese el nombre de la estacion: ")
            #lista_diccs= json.loads(docSensores_json)
            if estacionValida(nombre,Lista_diccs) :
                estacion = obtenerPosEstacion(nombre,Lista_diccs)
                imprimirSensoresEstacion(Lista_diccs[estacion])
            else :
                print("La estacion no se encuetra")
            opcion = input("Desea ingresar otra estacion? s/n ")
            listoEstacionSensores = opcion == 'n'
    elif opcion == 14 :
        print("La estacion con menos bateria es: {}".format(Lista_diccs[encontrarMenor(generarPromedios(Lista_diccs))].get('nombre')))
        #print(Lista_diccs[encontrarMenor(generarPromedios(Lista_diccs))].get('nombre'))
        input("Presione ENTER para volver al menu\n")
    # elif opcion == 15 :
    #     print("La estacion con menos bateria es (se buscara en representacion xml): ")
    #     #llamada a la funcion - imprimir resultado
    #     input("Presione ENTER para volver al menu\n")
    else:
        salir = True

print("Muchas gracias por utilizar el programa.\n             Que tenga lindo dia.")