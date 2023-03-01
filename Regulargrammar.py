import random

alphabet = [0, 1]
variables = ["S", "A", "B", "C", "D"]
startingsymbol = "A"
# Reglas de producción basadas en el AFD construido en la práctica #2
productionrules = {"S": "A", "A": ["0B", "1C"], "B": ["0A", "1D"], "C": ["0D", "1A"], "D": ["1B", "0C"]}


def stringconstruction(wordlength: int):  # Itera sobre las reglas de producción para construir las cadenas.
    constructedstring = ""
    i = 0
    actualsymbol = startingsymbol

    while i < wordlength:

        posibilities = productionrules.get(actualsymbol)  # Lado derecho de la transicion

        if (i == wordlength - 1) & (actualsymbol == "A" or actualsymbol == "D"):
            chosedtransition = posibilities[
                1]  # Evitando que la cadena quede completa en el estado B, que no es aceptable.
        else:
            chosedtransition = posibilities[
                random.randint(0, 1)]  # Accedo a un numero aleatorio entre 0 y 1 para escoger una transición al azar.

        newdigit = chosedtransition[:1]  # Dígito a añadir a la cadena
        constructedstring = constructedstring + newdigit  # Concateno a la cadena

        actualsymbol = chosedtransition[1:]  # Caracter no terminal al que voy a ir
        i = i + 1

    return constructedstring

    # Recorre las reglas de producción, agrega a la cadena, hasta que haya llegado a la longitud deseada.

    # En cada iteración toma un elemento al azar del lado derecho de la producción,
    # lo divide en su parte terminal y no terminal, concatena la terminal y continua el proceso.
    # Una vez llegado a la longitud deseada, retorna la cadena


def generatelanguage(wordlength: int,
                     wordquantity: int):  # Genera las palabras del lenguajes, con una longitud concreta
    language = []
    i = 0
    while i < wordquantity:
        language.append(stringconstruction(wordlength))
        i = i + 1
    return language

# Ejecuto el metodo stringconstruction hasta que haya generado la cantidad deseada de palabras,
# retorno una lista con lo generado.

testlanguage = generatelanguage(15, 30)

print(testlanguage)
