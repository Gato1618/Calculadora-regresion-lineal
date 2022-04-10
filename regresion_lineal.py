from math import pow


def ingreso_datos() -> list:
    """
    Se ingresan los datos correspondientes a x e y
    retorna una tupla con la lista de los x, y la lista de los y

    :return: lista con dos listas
    """
    n = 0
    lista_x = []
    lista_y = []

    # llenado de la lista de x
    while True:
        ingreso_x = input('Ingrese valor de x (next para romper el ciclo): ')
        if ingreso_x == 'next':
            break
        lista_x.append(float(ingreso_x))
        n += 1

    print('\n')

    # llenado de la lista de y
    for _ in range(0, n):
        ingreso_y = input('Ingrese valor de y: ')
        lista_y.append(float(ingreso_y))

    # retornar la lista
    return [lista_x, lista_y]


def calcular_regresion(lista_x_y: list) -> None:
    """
    calcula una regresion lineal e imprime en pantalla los resultados de los
    calculos

    :param lista_x_y: lista con los datos correspondientes a x e y
    :return: none
    """
    print('\n')

    # obtener la listas de los valores de x e y
    lista_x = lista_x_y[0]
    lista_y = lista_x_y[1]

    # cuantos datos hay
    n = len(lista_x_y[0])

    # calcular la suma de x, y, x*y, x^2
    contador = 0
    suma_x = 0
    suma_y = 0
    suma_xy = 0
    suma_x_cuadrado = 0
    print('i  x  y  xy  x^2')
    for _ in lista_x:
        i = contador + 1
        x = lista_x[contador]
        y = lista_y[contador]
        xy = round(x * y, 6)
        x_cuadrado = round(pow(x, 2), 6)
        print(f'{i}  {x}  {y}  {xy}  {x_cuadrado}')
        suma_x += x
        suma_y += y
        suma_xy += xy
        suma_x_cuadrado += x_cuadrado
        contador += 1

    suma_x_redondeada = round(suma_x, 6)
    suma_y_redondeada = round(suma_y, 6)
    suma_xy_redondeada = round(suma_xy, 6)
    suma_x_cuadrado_redondeada = round(suma_x_cuadrado, 6)

    print('\n')

    print('suma x')
    print(suma_x_redondeada)
    print('suma y')
    print(suma_y_redondeada)
    print('suma xy')
    print(suma_xy_redondeada)
    print('suma x^2')
    print(suma_x_cuadrado_redondeada)

    print('\n')

    # calcular pendiente(a) y el intercepto(b) de la regresion
    a = ((suma_x * suma_y) - n * suma_xy) / (pow(suma_x, 2) - n * suma_x_cuadrado)
    b = (suma_y - a * suma_x) / n
    a_redondeado = round(a, 6)
    b_redondeado = round(b, 6)
    print(f'a = {a_redondeado} \nb = {b_redondeado}')

    print('\n')

    # calcular valor necesario para obtener el valor de R cuadrado
    y_corchetes = suma_y / n
    y_corchetes_redondeado = round(y_corchetes, 6)
    print(f'<y> = {y_corchetes_redondeado}')

    print('\n')

    # calcular valor numerico de Xi cuadrado y un valor necesario para obtener el valor de R cuadrado
    contador = 0
    xi_cuadrado = 0
    suma_y_corchete = 0
    for _ in lista_x:
        elemento_xi_cuadrado = round(pow(a * lista_x[contador] + b - lista_y[contador], 2), 6)
        elemento_y = round(pow(lista_y[contador] - y_corchetes, 2), 6)
        xi_cuadrado += elemento_xi_cuadrado
        suma_y_corchete += elemento_y
        print(f'i = {contador + 1}')
        print('(ax + b - y)^2')
        print(f'{elemento_xi_cuadrado}')
        print('(y - <y>)^2')
        print(f'{elemento_y}')
        print('\n')
        contador += 1

    print('\n')

    # calculo de R cuadrado
    r = 1 - (xi_cuadrado / suma_y_corchete)
    r_redondeado = round(r, 6)
    xi_cuadrado_redondeado = round(xi_cuadrado, 6)
    print(f'r cuadrado = {r_redondeado} \nxi cuadrado = {xi_cuadrado_redondeado}')


# ejecutar le programa
lista_datos = ingreso_datos()
calcular_regresion(lista_datos)
