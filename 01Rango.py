#v


import pandas as pd

inicio = int(input('Introduce el año inicial de ventas : '))
fin = int(input('Introduce el añofinal de ventas: '))
ventas = {}

for i in range(inicio, fin+1):
    ventas[i] = float(input('Introduce las ventas de el año ' + str(i) + ':'))
    
    ventas = pd.Series(ventas)
    print('Ventas \n', ventas)
    print('Ventas con Descuento\n', ventas*0.9)
    