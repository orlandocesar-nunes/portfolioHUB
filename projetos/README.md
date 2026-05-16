# 💻 Documentação dos Projetos em Python

Este diretório contém os códigos-fonte dos projetos práticos desenvolvidos durante o 1º semestre de Engenharia de Software. O foco principal de cada script é a aplicação de lógica de programação estruturada, tratamento de exceções e manipulação de dados.

## 🛠️ Tecnologias e Ambiente
* **Linguagem:** Python 3.x
* **Ambiente de Desenvolvimento:** Thonny IDE / VS Code
* **Bibliotecas:** Apenas bibliotecas nativas (ex: `base64`).

---

## 📂 Lista de Projetos

### 1. Codificador e Decodificador Base64 (`base64_converter.py`)
Script projetado para demonstrar o empacotamento de dados para tráfego em rede.
* **Lógica aplicada:** Conversão de tipos (`str` para `bytes`), uso da biblioteca nativa `base64` e blocos de `try/except` para prevenir que o programa quebre caso o usuário insira uma string inválida na hora de decodificar.

### 2. Calculadora Interativa Segura (`calculadora.py`)
Calculadora via terminal focada em blindagem contra erros do usuário.
* **Lógica aplicada:** Estruturas condicionais encadeadas (`if/elif/else`). Implementação de travas de segurança matemáticas, como a verificação e bloqueio de divisões por zero antes da execução do cálculo.

### 3. Engine de Notas com Sentinela (`sistema_notas.py`)
Processador em lote para cálculo de médias escolares.
* **Lógica aplicada:** Uso de laço de repetição condicional (`while True`) associado a um valor "sentinela" para interrupção do loop. Utiliza variáveis contadoras e acumuladoras de memória para processar os dados em tempo real.

### 4. Filtro de Paridade e Sequências (`filtro_numeros.py`)
Algoritmo de separação e estruturação de dados numéricos.
* **Lógica aplicada:** Operador de módulo matemático (`%`) para teste de paridade e uso da função `range()` para geração automatizada de listas crescentes e decrescentes.

---
*Documentação mantida e versionada por Orlando César.*
