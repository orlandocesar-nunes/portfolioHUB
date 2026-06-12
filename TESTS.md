# Relatório de Testes e Validação - PortfolioHUB

## 1. Testes de Integração Web (GitHub Pages)
- [x] **Disponibilidade:** O site portfólio está no ar e acessível via link público.
- [x] **Navegação:** O armazenamento estático está carregando corretamente.
- [x] **Redirecionamento:** Os hiperlinks da interface direcionam corretamente para o código-fonte dos projetos em Python no repositório.

## 2. Testes de Software (Scripts Python)
- [x] `calculadora.py`: Testes de estresse com divisão por zero e inserção de letras no lugar de números. O bloco `try/except` preveniu a quebra do sistema.
- [x] `conversor_base64.py`: Validação de codificação e decodificação de strings operando com sucesso.
- [x] `gerenciador.py`: Funções de CRUD (adicionar, listar, remover tarefas) executadas sem erros lógicos no terminal.

## 3. Testes de Segurança e Configuração
- [x] Arquivo `SECURITY.md` acessível e legível.
- [x] Auditoria visual: Nenhuma chave de API, senha ou dado sensível exposto nos códigos.
- [x] Bloqueio de commits diretos não autorizados testado (Acesso exclusivo via SSO Google do Administrador).