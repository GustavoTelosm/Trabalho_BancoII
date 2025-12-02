TRABALHO DE BANCO DE DADOS SEMIESTRUTURADOS

Alunos: Gustavo Henrique Teló, Arthur Couto Mulling


Curso: Ciência da Computação

DESCRIÇÃO DO PROJETO:
Este projeto realiza a integração de dados relacionais (PostgreSQL) com dados semiestruturados (XML) utilizando a linguagem Python. A aplicação lê registros de transações de um arquivo XML e realiza a junção (JOIN) com os dados cadastrais das peças armazenados no banco de dados.

ARQUIVOS DO REPOSITÓRIO:
1. app.py: Código fonte da aplicação em Python (comentado).
2. postcriatab.sql: Script SQL original para criação e população do banco de dados.
3. Fornecimento.xml: Arquivo de dados semiestruturados utilizado na integração.
4. Backup_Trabalho...: Arquivo de backup do banco (formato Tar/Custom).

PRÉ-REQUISITOS:
- Python 3.x instalado.
- Biblioteca 'psycopg2' instalada via pip.
  Comando: pip install psycopg2-binary
- Servidor PostgreSQL ativo.

INSTRUÇÕES DE CONFIGURAÇÃO (IMPORTANTE):
Antes de executar o arquivo 'app.py', é necessário ajustar as credenciais de acesso ao banco de dados no início do código.

1. Abra o arquivo 'app.py' no VS Code ou editor de preferência.
2. Localize a seção "CONFIGURAÇÃO" (linhas iniciais).
3. Altere as seguintes variáveis conforme o seu ambiente local:
   - SENHA_DO_BANCO: Insira a senha do seu usuário 'postgres'.
   - NOME_DO_BANCO: Insira o nome do banco de dados criado (o script padrão utiliza 'Trabalho').

OBSERVAÇÃO TÉCNICA:
O código foi adaptado para ler a coluna 'cdade' na tabela 'Peca', mantendo a consistência com o script original 'postcriatab.sql' fornecido, que contém esta grafia específica na DDL da tabela.

COMO EXECUTAR:
1. Certifique-se de que o banco de dados foi criado rodando o script 'postcriatab.sql'.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:
   
   py app.py
   
   (Ou 'python app.py' dependendo da configuração do seu sistema).


O resultado será exibido no console, apresentando a tabela integrada com dados do SQL (Nome, Cor, Cidade) e do XML (Quantidade, Valor).
