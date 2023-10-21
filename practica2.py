def procesar_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(f'Clave: {clave}, Valor: {valor}')

def funcion_con_parametro_por_defecto(parametro=10):
    return parametro

def funcion_con_varios_valores():
    return 1, 2, 3

diccionario_ejemplo = {'a': 1, 'b': 2, 'c': 3}
procesar_diccionario(diccionario_ejemplo)

valor = funcion_con_parametro_por_defecto()
print(f'Valor por defecto: {valor}')

valores = funcion_con_varios_valores()
print(f'Valores múltiples: {valores}')
