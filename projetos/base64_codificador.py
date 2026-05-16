import base64

def esconder_mensagem(texto):
    texto_em_bytes = texto.encode('utf-8')
    texto_codificado = base64.b64encode(texto_em_bytes)
    return texto_codificado.decode('utf-8')

def revelar_mensagem(codigo):
    try:
        codigo_em_bytes = codigo.encode('utf-8')
        texto_original = base64.b64decode(codigo_em_bytes)
        return texto_original.decode('utf-8')
    except:
        return "ERRO: Código inválido. Não foi possível decifrar."

print("=========================================")
print("    MÁQUINA DE MENSAGENS SECRETAS   ")
print("=========================================")

while True:
    print("\nO que você deseja fazer?")
    print("1 - Esconder uma mensagem")
    print("2 - Revelar uma mensagem secreta")
    print("3 - Sair do programa")
    
    escolha = input("\nDigite a sua opção (1, 2 ou 3): ")
    
    if escolha == '1':
        mensagem = input("\nDigite a frase que você quer esconder: ")
        resultado = esconder_mensagem(mensagem)
        print("\nSUA MENSAGEM SECRETA É:")
        print(resultado)
        print("-" * 40)
        
    elif escolha == '2':
        codigo = input("\nCole o código secreto aqui: ")
        resultado = revelar_mensagem(codigo)
        print("\nA MENSAGEM ORIGINAL ERA:")
        print(resultado)
        print("-" * 40)
        
    elif escolha == '3':
        print("\nSaindo do sistema. Até logo!")
        break
        
    else:
        print("\nOpção inválida. Digite 1, 2 ou 3.")