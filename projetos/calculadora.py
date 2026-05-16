print("=========================================")
print("     CALCULADORA INTERATIVA SEGURA       ")
print("=========================================")

try:
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Escolha a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    print("-" * 40)
    
    if operacao == '+':
        print(f"Resultado: {num1} + {num2} = {num1 + num2}")
    elif operacao == '-':
        print(f"Resultado: {num1} - {num2} = {num1 - num2}")
    elif operacao == '*':
        print(f"Resultado: {num1} * {num2} = {num1 * num2}")
    elif operacao == '/':
        if num2 == 0:
            print(" ERRO DE SEGURANÇA: Bloqueio ativado. Não é possível dividir por zero!")
        else:
            print(f"Resultado: {num1} / {num2} = {num1 / num2:.2f}")
    else:
        print(" ERRO: Operação matemática inválida.")

except ValueError:
    print(" ERRO CRÍTICO: Entrada inválida. Por favor, digite apenas números.")