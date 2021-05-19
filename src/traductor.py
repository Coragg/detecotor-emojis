def censura(texto_original):
    palabra = input("Ingrese palabra:")
    i = 0
    nuevo = ""
    while i < len(texto_original):
        if palabra == texto_original[i:i + len(palabra)]:
            nuevo += "*" * len(palabra)
            i += len(palabra)
        else:
            nuevo += texto_original[i]
            i += 1
    print("Texto censurado: ", nuevo)
        