# 🚀 portfolioHUB | Orlando César Nunes de Oliveira

<div align="center">
  <img src="eur.jpg" alt="Orlando César" width="160" style="border-radius: 50%; border: 3px solid #007acc;">
  <h1>Engenharia de Software</h1>
  <p><i>Documentação da minha trajetória de aprendizado e desenvolvimento de software</i></p>

  <a href="https://www.linkedin.com/in/orlando-cesar-nunes-de-oliveira-5691033b4/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="mailto:orlandocesar.2006nunes@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
</div>

---

## 1. Perfil Pessoal 👤

**Sobre a minha trajetória**
Sou Orlando César, estudante do 1º semestre de Engenharia de Software no CEUB, em Brasília. Minha escolha por essa área surgiu da curiosidade de entender a lógica por trás das tecnologias que usamos diariamente. Não me contento apenas em ver um programa funcionar; eu gosto de abrir o capô, ler a documentação, entender como a máquina processa os dados e, principalmente, descobrir por que o código quebrou e como consertá-lo.

Acredito que um bom desenvolvedor se forma na capacidade de resolver problemas de forma estruturada. Por isso, meu foco atual tem sido dominar a lógica de programação de ponta a ponta. Quando pego um desafio, prefiro gastar tempo entendendo o comportamento dos dados e desenhando a arquitetura mental do sistema antes de começar a digitar. 

No trabalho em equipe, sou direto e prezo pela clareza. Gosto de escrever códigos que outras pessoas consigam ler e entender, documentando os processos e mantendo uma comunicação sempre aberta com colegas e mentores.

**Onde me encontrar:**
* 📧 **E-mail:** [orlandocesar.2006nunes@gmail.com](mailto:orlandocesar.2006nunes@gmail.com)
* 📍 **Localização:** Brasília - DF
* 📱 **WhatsApp:** (61) 98450-3429
* 💼 **LinkedIn:** [Acesse meu perfil profissional](https://www.linkedin.com/in/orlando-cesar-nunes-de-oliveira-5691033b4/)

---

## 2. Currículo 📄

[📥 **Clique aqui para baixar o meu Currículo completo em formato PDF**](./curriculo-orlando.pdf)

### 🎯 Objetivo Profissional
Estou em busca da minha primeira oportunidade profissional como estagiário na área de Engenharia de Software ou Desenvolvimento. Quero vivenciar o ritmo de uma equipe de tecnologia real, contribuir com meus conhecimentos em lógica de programação e Python, e absorver as melhores práticas de mercado para escrever códigos limpos e escaláveis.

### 🎓 Formação Acadêmica
* **Bacharelado em Engenharia de Software** | CEUB - Centro Universitário de Brasília
  * *Período:* 1° semestre (2026 - Presente).
  * *Foco de estudo atual:* Algoritmos, Matemática Computacional e Lógica de Programação estruturada.
* **Ensino Médio** | Colégio Batista Windermere (Concluído em 2023).

### 💻 Habilidades Técnicas (Hard Skills)
* **Python 3:** Desenvolvimento de scripts com foco em manipulação de tipos de dados, estruturas condicionais avançadas, laços de repetição iterativos (`for/while`), tratamento de erros e conversão de strings para bytes.
* **Ferramentas e IDEs:** Prática constante com o Thonny (excelente para visualizar a execução do código passo a passo) e VS Code.
* **Versionamento:** Uso de Git e GitHub para hospedar projetos, gerenciar versões do meu código e escrever documentações usando Markdown.

---

## 3. Projetos Acadêmicos e Profissionais 💻

👉 [🔗 **Clique aqui para acessar o repositório oficial com todos os códigos-fonte no GitHub**](https://github.com/orlandocesar-nunes/portfolioHUB/tree/main/projetos)

### 🚀 Projeto: Codificador e Decodificador Base64 (base64_converter.py)
Este foi meu primeiro projeto autônomo, criado para ir além da sala de aula e entender como os dados trafegam pela rede. Desenvolvi um programa capaz de converter mensagens de texto comuns para o padrão Base64 e fazer o caminho inverso. Tudo foi construído e testado no ambiente do Thonny e VS Code.
* **A grande lição:** Descobri na prática que Base64 não é criptografia (não esconde a informação como uma senha), mas sim um formato de *codificação*. Ele serve para empacotar o texto de um jeito seguro para que viaje pela rede sem corromper a leitura, mantendo os caracteres sempre legíveis.
* **Implementação técnica:** Utilizei bibliotecas nativas do Python para não depender de instalações externas. Trabalhei diretamente com a conversão de strings para o formato de *bytes* e implementei blocos de tratamento de erro para garantir que, se o usuário digitar uma string inválida na hora de decodificar, o programa exiba um aviso amigável em vez de fechar abruptamente.

### 🧮 Calculadora Interativa e Tratamento de Exceções (calculadora.py)
Criei um sistema de cálculos matemáticos no terminal. O foco técnico desse projeto foi a robustez. Utilizando estruturas condicionais encadeadas (`if/elif/else`), criei travas de segurança na lógica. Por exemplo, o código identifica tentativas de divisão por zero e bloqueia a operação, evitando o travamento do sistema.

### 📊 Engine de Análise de Desempenho Escolar (sistema_notas.py)
Desenvolvi um script de processamento em lote. O programa permite inserir notas de uma turma inteira através de um loop infinito (`while True`). A sacada lógica foi implementar um "sentinela" (uma condição de parada específica, como digitar -1) para interromper o laço. Nos bastidores, o código usa variáveis como acumuladores e contadores para calcular a média final e a taxa de aprovação em tempo real.

### 🔢 Filtro Analítico de Sequências e Paridade (filtro_numeros.py)
Um programa voltado para estruturação de dados. Ele recebe valores e utiliza o operador de módulo (`%`) para separar matematicamente o que é par do que é ímpar. Também implementei a função `range()` para gerar progressões numéricas ordenadas, conseguindo extrair médias isoladas apenas de grupos específicos de números.

### 📝 Gerenciador de Tarefas - To-Do List (gerenciador_tarefas.py)
Um aplicativo de terminal completo para organizar o dia a dia, permitindo criar, visualizar, marcar como concluída e remover tarefas. Demonstra o conceito de CRUD básico (Create, Read, Update, Delete) e utiliza estruturas complexas como listas e dicionários para manipular os dados dinamicamente, além de validações robustas com `try/except`.

---

## 4. Habilidades e Competências 🛠️

Para demonstrar minhas competências de forma mais dinâmica, criei uma apresentação visual que detalha meu perfil técnico, minha capacidade de resolução de problemas e minhas habilidades comportamentais (Soft Skills) no dia a dia.

[🎨 **CLIQUE AQUI para abrir a minha apresentação de Habilidades no Canva**](https://www.canva.com/design/DAHF1Y5vZpM/h_nSjKXd68rTRhDcnz9vPg/view)

---

## 5. Recomendações e Testemunhos 🤝

Como estou no início da minha jornada na graduação, a recomendação abaixo reflete o perfil acadêmico que venho consolidando junto aos meus professores através da entrega das minhas atividades práticas e projetos de código:

> *"Durante as práticas de programação, o Orlando tem se mostrado um aluno extremamente analítico e focado na resolução de problemas. Ele não busca apenas o resultado fácil; nota-se a preocupação dele em escrever códigos limpos, entender o fluxo dos dados e resolver falhas lógicas de maneira independente. A sua capacidade de documentar e explicar processos técnicos de forma clara demonstra que ele tem a mentalidade exata que o mercado de Engenharia de Software exige."*
> 
> **— Perfil Acadêmico Validado nas Disciplinas Práticas (CEUB, 2026)**

---

## 6. Outros (Formação Extra e Conhecimentos) 📚

Acredito que o aprendizado em tecnologia não deve se restringir apenas à grade curricular. Por isso, busco expandir meu conhecimento técnico em áreas complementares:

* **Estudos em Inteligência Artificial:** Realizei cursos introdutórios (2026) para compreender o funcionamento dos modelos de linguagem. O objetivo não é depender da IA para programar, mas sim aprender a usá-la como uma ferramenta de auxílio para depurar códigos, gerar dados de teste e acelerar pesquisas em documentações extensas.
* **Processamento Digital de Imagens:** Tive um contato inicial com o processamento de imagens usando softwares livres (2026). Essa experiência foi essencial para entender como a máquina processa informações visuais, lidando com matrizes de dados e manipulação de pixels.
* **Inglês Técnico (Intermediário):** Consigo ler, interpretar e traduzir documentações oficiais (como a do Python.org), guias de bibliotecas e soluções em fóruns como o Stack Overflow, algo indispensável no fluxo de trabalho de qualquer desenvolvedor.

---

<div align="center">
  <sub>Repositório construído e atualizado por Orlando César • 12/04/2026</sub>
</div>
