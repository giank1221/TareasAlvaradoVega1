
def separa_letras(Cadena):  # creacion del modulo que separa letras

    if isinstance(Cadena, str):  # Chequea que "Cadena" sea un str

        if Cadena.isalpha() or Cadena == "":
            # Chequea que "Cadena" contenga solo letras, ademas deja pasar el
            # caso que contiene un str vacio

            if Cadena != "":        # Chequea que "Cadena" no sea un str vacio
                res1 = ""           # Define a res 1 como un str vacio
                res2 = ""           # Define a res 1 como un str vacio
                res1 = res1.join(c for c in Cadena if c.isupper())
                # Introduce en res1 las mayusculas
                res2 = res2.join(c for c in Cadena if c.islower())
                # Introduce en res2 las minusculas
                return 0, res1, res2
                # Al estar correcto devuelve codigo 0, res1 y res2

            else:                        # Al estar vacio devuelve el codigo
                return -300, None, None  # de error -300 y None en 1 y 2

        else:                            # Al no contener letras devuelve el
            return -200, None, None      # error -200 y None en res1 y res2

    else:                        # En caso de no ser un str devuelve el
        return -100, None, None  # codigo -100, y None para res1 y res2


def potencia_manual(base, potencia):  # creacion del modulo potencia manual

    resultado = 1                     # Definicion de variable local

    if isinstance(potencia, int) and isinstance(base, int):
        # Chequea que potencia y base sean enteros

        if potencia > 0:  # Si potencia es mayor a 0 se realiza la operacion

            for _ in range(potencia):
                # Se hace un for que tiene de limite potencia

                resultado = resultado * base
                # Se define resultado como resultado por base, una vez, luego
                # se repite por estar dentro de un for
            return 0, resultado
            # Al estar correcto devuelve codigo 0, resultado

        else:   # Para el caso especial en el que la potencia sea cero

            return 0, resultado
            # Al estar correcto devuelve codigo 0, resultado

    else:                  # En caso de no ser potencia o base ambos enteros,
        return -400, None  # brinda codigo de error -400 y resultado None
