print("=========================================")
print("      ENGINE DE NOTAS COM SENTINELA      ")
print("=========================================")
print("Instrução: Digite as notas dos alunos. Digite -1 para calcular a média e sair.\n")

soma_notas = 0.0 
contador = 0       

while True:
    try:
        nota = float(input("Digite uma nota de 0 a 10 (ou -1 para encerrar): "))
        
        if nota == -1:
            break
            
        if nota < 0 or nota > 10:
            print(" -> Aviso: Nota fora do limite. Tente novamente.")
            continue
            
        soma_notas += nota
        contador += 1
        
    except ValueError:
        print(" -> Erro: Digite um valor numérico válido.")

print("\n" + "=" * 40)
print("             PROCESSAMENTO FINAL         ")
print("=" * 40)

if contador > 0:
    media = soma_notas / contador
    print(f"Total de notas processadas: {contador}")
    print(f"Média final da turma: {media:.2f}")
else:
    print("Nenhuma nota foi inserida no sistema.")