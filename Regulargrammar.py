class Regulargrammar:

    alphabet = [0,1]
    variables = ["S","A","B","C","D"]
    startingsymbol = "S"
    # Reglas de producción basadas en el AFD construido en la práctica #2
    productionrules = {"S": "A", "A": ["0B","1C",""], "B":["0A","1D"], "C": ["0D","1A",""], "D":["0C","1B",""]}

    def stringconstruction(wordlength: int):   # Itera sobre las reglas de producción para construir las cadenas.
        
        # Recorre las reglas de producción, agrega a la cadena, hasta que haya llegado a la longitud deseada.

        # En cada iteración toma un elemento al azar del lado derecho de la producción,
        # lo divide en su parte terminal y no terminal, concatena la terminal y continua el proceso.
        # Una vez llegado a la longitud deseada, sale usando el elemento vacío ""
        pass

    def generateLanguage(wordlength: int, wordquantity: int):   # Genera las palabras del lenguajes, con una longitud concreta
        
        # Ejecuto el metodo stringconstruction hasta que haya generado la cantidad deseada de palabras,
        # retorno una lista con lo generado.
        pass
        
        

test = Regulargrammar().productionrules

print(test)
