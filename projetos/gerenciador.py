import os

tarefas = []
proximo_id = 1

def limpar_tela():
    """Função auxiliar para limpar o terminal e melhorar a visualização."""
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_tarefa():
    """Cria uma nova tarefa com status pendente."""
    global proximo_id
    print("\n--- Adicionar Nova Tarefa ---")
    descricao = input("Digite a descrição da tarefa: ").strip()
    
    if descricao:
        tarefa = {
            'id': proximo_id,
            'descricao': descricao,
            'concluida': False
        }
        tarefas.append(tarefa)
        print(f"✔️ Tarefa '{descricao}' adicionada com ID {proximo_id}.")
        proximo_id += 1
    else:
        print("Erro: A descrição da tarefa não pode estar vazia.")

def visualizar_tarefas():
    """Exibe todas as tarefas cadastradas e seus status."""
    print("\n--- Suas Tarefas ---")
    if not tarefas:
        print("Sua lista está vazia. Adicione uma tarefa!")
    else:
        print(f"{'ID':<5} | {'Status':<10} | {'Descrição'}")
        print("-" * 50)
        for t in tarefas:
            status = "✅ Fone" if t['concluida'] else "⏳ Pendente"
            print(f"{t['id']:<5} | {status:<10} | {t['descricao']}")
    print("-" * 50)

def concluir_tarefa():
    """Localiza uma tarefa pelo ID e marca como concluída."""
    visualizar_tarefas()
    if not tarefas: return

    try:
        id_busca = int(input("\nDigite o ID da tarefa que deseja concluir: "))
        encontrada = False
        for t in tarefas:
            if t['id'] == id_busca:
                t['concluida'] = True
                print(f"✔️ Tarefa {id_busca} marcada como concluída!")
                encontrada = True
                break
        if not encontrada:
            print(f"⚠️ Erro: Não foi encontrada nenhuma tarefa com o ID {id_busca}.")
    except ValueError:
        print("⚠️ Erro: Por favor, digite um número de ID válido.")

def remover_tarefa():
    """Remove uma tarefa da lista baseada no ID."""
    visualizar_tarefas()
    if not tarefas: return

    try:
        id_busca = int(input("\nDigite o ID da tarefa que deseja REMOVER: "))
        tarefa_para_remover = None
        for t in tarefas:
            if t['id'] == id_busca:
                tarefa_para_remover = t
                break
        
        if tarefa_para_remover:
            tarefas.remove(tarefa_para_remover)
            print(f"❌ Tarefa '{tarefa_para_remover['descricao']}' removida com sucesso.")
        else:
            print(f"⚠️ Erro: Não foi encontrada nenhuma tarefa com o ID {id_busca}.")
    except ValueError:
        print("⚠️ Erro: Por favor, digite um número de ID válido.")

# =========================================
#             MENU PRINCIPAL
# =========================================
print("=========================================")
print(" 📝📝📝 SISTEMA DE TO-DO LIST 📝📝📝 ")
print("=========================================")

while True:
    print("\nO que você deseja fazer?")
    print("1 - Adicionar tarefa")
    print("2 - Visualizar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Sair do programa")
    
    escolha = input("\nDigite a sua opção (1-5): ")
    
    if escolha == '1':
        limpar_tela()
        adicionar_tarefa()
    elif escolha == '2':
        limpar_tela()
        visualizar_tarefas()
    elif escolha == '3':
        limpar_tela()
        concluir_tarefa()
    elif escolha == '4':
        limpar_tela()
        remover_tarefa()
    elif escolha == '5':
        print("\nSaindo do sistema. Organize-se sempre!")
        break
    else:
        print("\nOpção inválida. Digite um número entre 1 e 5.")