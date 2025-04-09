# Projeto CRUD com Tkinter e SQLite
Este é um projeto de exemplo que implementa uma interface gráfica simples usando Tkinter para a manipulação de dados de usuários em um banco de dados SQLite. O projeto oferece funcionalidades para inserir, buscar, atualizar e excluir registros de usuários.

## Funcionalidades
- <b>Inserir um novo usuário no banco de dados.</b>
- <b>Buscar informações de um usuário pelo seu ID.</b>
- <b>Atualizar dados de um usuário existente.</b>
- <b>Cadastro de Clientes</b>: Interface para adicionar novos clientes ao sistema.
- <b>Excluir um usuário do banco de dados.</b>

## Pré-requisitos
- <b>Python 3.15.2 instalado.</b>
- <b>Bibliotecas Tkinter e SQLite já estão incluídas na instalação padrão do Python.</b>

## Instalação
<b>Para instalar e executar o sistema localmente, siga os passos abaixo:</b>
1. Clonar o Repositório
- Primeiro, clone o repositório do GitHub para o seu ambiente local:
``` bash
git clone https://github.com/Srleo12/Usuario_Tkinter/Usuario_Tkinter.git
cd Usuario_Tinter
```
2. Criar um Ambiente Virtual
- É recomendável criar um ambiente virtual para instalar as dependências:
```
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```
3. Execute o arquivo App.py para iniciar a aplicação:
- Instale as bibliotecas necessárias utilizando o pip:
```
python App.py
```

## Estrutura do Projeto
- <b>App.py</b>: Arquivo principal que contém a interface gráfica da aplicação.
- <b>Banco.py</b>: Contém a classe responsável pela conexão e criação da tabela no banco de dados.
- <b>Usuarios.py</b>: Contém a classe que implementa as operações CRUD no banco de dados (inserir, alterar, buscar, atualizar e deletar).

## Como Usar
- <b>Ao iniciar a aplicação, uma janela gráfica será aberta.</b>
- <b>Insira os dados nos campos de texto e clique nos botões para realizar as operações (inserir, buscar, atualizar, excluir).</b>
- <b>Mensagens de status serão exibidas na parte inferior da janela para indicar o sucesso ou falha das operações.</b>

## Considerações Finais
<b>Este sistema foi desenvolvido como um exemplo básico de CRUD (Create, Read, Update, Delete) utilizando Tkinter e SQLite. Ele pode ser expandido conforme a necessidade, adicionando novas funcionalidades ou melhorando as já existentes.</b>

## Contribuição
Sinta-se à vontade para abrir issues e enviar pull requests para melhorias neste projeto!
