palabra = input("Escribe una palabra: ")

for i in range(len(palabra) // 2):
    j = len(palabra) - 1 - i
    if palabra[i] != palabra[j]:
        print("No es palíndromo")
        break
else:
    print("Sí es palíndromo")
