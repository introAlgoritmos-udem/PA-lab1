# -*- coding: utf-8 -*-
"""
Este programa numero de meses entre dos años ingresados por el usuario

@author: pensamiento-algoritmico
"""

# Entrada de los años inicial y final
yearInit = int(input("Ingrese el año inicial: "))
yearEnd = int(input("Ingrese al año final: "))

# Calculos
years = yearEnd - yearInit
months = 12*years

# Despliegue de los meses
print("El numero de meses entre", yearInit, "y", yearEnd, "es", months)