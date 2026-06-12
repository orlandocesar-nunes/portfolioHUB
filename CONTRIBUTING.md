# Guia de Contribuição e Colaboração - PortfolioHUB

Este documento documenta o fluxo de trabalho e as práticas de controle de versão deste repositório, com o objetivo de facilitar o compartilhamento do código e futuras colaborações.

## 1. Fluxo de Versionamento (Git)
O desenvolvimento deste projeto segue um ciclo de integração contínua rigoroso:
- **`git add .`** -> Prepara as modificações testadas localmente.
- **`git commit -m`** -> Registra as alterações no histórico.
- **`git push`** -> Envia o código homologado para a branch `main` pública.

## 2. Padrões de Mensagem de Commit
Para manter a rastreabilidade do repositório, utilizamos prefixos padronizados nas mensagens:
- **`feat:`** Para adição de novos códigos ou funcionalidades.
- **`fix:`** Para correção de erros ou bugs nos scripts Python.
- **`docs:`** Para alterações nos arquivos de documentação (README, SECURITY, etc).

## 3. Como Compartilhar e Testar (Para Avaliadores)
A arquitetura do repositório é aberta. Qualquer desenvolvedor ou avaliador pode clonar este projeto para analisar o código-fonte em sua própria máquina rodando o seguinte comando no terminal:

```bash
git clone [https://github.com/orlandocesar-nunes/portfolioHUB.git](https://github.com/orlandocesar-nunes/portfolioHUB.git)