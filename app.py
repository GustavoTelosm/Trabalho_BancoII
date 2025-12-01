import psycopg2  # Biblioteca para conectar o Python ao PostgreSQL 
import xml.etree.ElementTree as ET  # Biblioteca padrão do Python para ler arquivos XML


# Definição das credenciais que configurei na instalação do banco
SENHA_DO_BANCO = '5525'
NOME_DO_BANCO = 'Trabalho' # Nome exato que aparece no pgAdmin

def conectar():
    """
    Função para estabelecer a conexão.
    Usei try/except para tratar erros caso o banco esteja desligado ou senha errada.
    """
    try:
        # A opção 'client_encoding=utf8' foi necessária para evitar erros de acentuação no Windows
        conn = psycopg2.connect(
            dbname=NOME_DO_BANCO,
            user='postgres',
            password=SENHA_DO_BANCO,
            host='localhost',
            port='5432',
            options='-c client_encoding=utf8'
        )
        return conn
    except Exception as erro:
        print(f"\nERRO CRÍTICO: Não foi possível conectar ao banco '{NOME_DO_BANCO}'.")
        print(f"Detalhe do erro: {erro}")
        return None

def main():
    print("--- INICIANDO APLICAÇÃO DE INTEGRAÇÃO (ETAPA 2) ---")
    

    conn = conectar()
    if not conn:
        return # Se não conectar, encerra o programa aqui.

    # O 'cursor' é o objeto que permite executar comandos SQL pelo Python
    cur = conn.cursor()
    
  
    try:
        sql_query = "SELECT cod_peca, pnome, cor, cdade FROM Peca"
        cur.execute(sql_query)
    except Exception as e:
        print(f"Erro ao executar a consulta SQL: {e}")
        return


    pecas_sql = {}
    
    # fetchall() traz todas as linhas do banco
    for linha in cur.fetchall():
        id_peca = linha[0]
        # Estruturando os dados em memória
        pecas_sql[id_peca] = {
            'nome': linha[1], 
            'cor': linha[2], 
            'cidade': linha[3] # Aqui normalizei o nome para 'cidade' no meu objeto
        }
    
    conn.close() # Boa prática: fechar a conexão assim que terminar de usar.
    print(f"Status: Conexão bem sucedida. {len(pecas_sql)} peças carregadas do PostgreSQL.")


    try:
        # O ElementTree faz o 'parse' da estrutura de árvore do XML
        tree = ET.parse('Fornecimento.xml')
        root = tree.getroot() # Pega a raiz do documento
    except FileNotFoundError:
        print("ERRO: O arquivo 'Fornecimento.xml' não foi encontrado na pasta do projeto.")
        return


    print("\n" + "="*90)
    print("RELATÓRIO INTEGRADO: DADOS RELACIONAIS (SQL) + SEMIESTRUTURADOS (XML)")
    print("="*90)
    # Formatação de string para alinhar as colunas na tela
    print(f"{'CÓD':<5} | {'NOME (SQL)':<15} | {'COR (SQL)':<10} | {'CIDADE (SQL)':<12} | {'QTD (XML)':<10} | {'VALOR (XML)'}")
    print("-" * 90)

    encontrados = 0
    
    # Loop para percorrer cada linha <row> do arquivo XML
    for row in root.findall('row'):
        # Extração dos dados do XML (convertendo tipos quando necessário)
        cod_peca_xml = int(row.find('cod_peca').text) 
        qtd = row.find('quantidade').text
        valor = row.find('valor').text

        
        # Verifico se o código da peça que veio do XML existe no meu dicionário do SQL.
        if cod_peca_xml in pecas_sql:
            # Se existir, recupero os dados complementares (Nome, Cor, Cidade)
            dados_complementares = pecas_sql[cod_peca_xml]
            
            # Imprimo a linha combinada
            print(f"{cod_peca_xml:<5} | {dados_complementares['nome']:<15} | {dados_complementares['cor']:<10} | {dados_complementares['cidade']:<12} | {qtd:<10} | {valor}")
            encontrados += 1

    print("-" * 90)
    print(f"Processamento finalizado. Total de registros integrados: {encontrados}")

# Garante que a função main() só rode se executarmos o arquivo diretamente
if __name__ == "__main__":
    main()