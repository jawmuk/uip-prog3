#!/usr/bin/python


'''
Este programa agarra dos variables y cuenta las veces que fue llamada la misma
'''

maxCalled = 0

minCalled = 0


def max_val(a, b):
    #''''Returns the maximum of the specified arguments.

    ''' Esta parte  dice cual es el numero mayor entre los 2 numeros ingresados

    :param a: Primer numero a comparar

    :type a: int

    :param b: Segundo numero a comparar

    :type b: int

    :return: Regresa el valor mas grande de los 2

    :rtype: int '''


    global maxCalled

    maxCalled = maxCalled + 1

    if (a > b):

        return a

    elif (b > a):

        return b

    else:

        return a


def min_val(a, b):
    '''

        Esta funcion nos proporciona el numero mas pequeño de los 2 ingresados

        :param a: Primer numero

        :type a: int

        :param b: Segundo numero

        :type b: int
        :return: Regresa el valor mas pequeño de los 2

        :rtype: int



        '''

    global minCalled

    minCalled = minCalled + 1

    if (a < b):

        return a

    elif (b < a):

        return b

    else:

        return a


def print_usage(init_msg, max_val=True, min_val=True):
    '''  Esta funcion sirve para decir la cuantas veces las funciones anteriores fueron llamadas



       :param init_msg: EL mensaje inicial a imprimir

       :type init_msg: str



       :param max_val: Esta variable sirve para saber si se va a imprimir la cantidad de veces usada la funcion max_val

       :type max_val: bool

       :param min_val: Esta variable sirve para saber si se va a imprimir la cantidad de veces usada  la funcion min_val

       :type min_val: bool '''
    global maxCalled, minCalled

    print(init_msg)

    if max_val:
        print('functin max_val was called', maxCalled, ' times')

    if min_val:
        print('function min_val was called', minCalled, ' times')


print('Calling function max_val')

print(max_val.__doc__)

max_val(1, 4)

max_val(2, b=1)

max_val(b=4, a=3)

print('Calling function min_val')

print(min_val.__doc__)

min_val(1, 4)

min_val(2, 4)

min_val(4, b=9)

print_usage('The usage of functions min_val and max_val')