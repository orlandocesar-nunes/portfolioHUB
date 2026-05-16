print("=========================================")
print("     FILTRO DE PARIDADE E SEQUÊNCIAS     ")
print("=========================================")

try:
    inicio = int(input("Digite o número inicial da sequência: "))
    fim = int(input("Digite o número final da sequência: "))
    
    pares = []
    impares = []
    
    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
            
    print("\n" + "-" * 40)
    print("             RESULTADOS                  ")
    print("-" * 40)
    
    print(f"Intervalo analisado: {list(range(inicio, fim + 1))}")
    print(f"Números Pares encontrados: {pares}")
    print(f"Números Ímpares encontrados: {impares}")

except ValueError:
    print("\nERRO: Por favor, insira apenas números inteiros para gerar a sequência.")