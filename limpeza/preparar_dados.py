import pandas as pd

def preparar_csv_para_mysql(nome_arquivo_entrada, nome_arquivo_saida, id_da_moeda):
    """
    Função para ler, limpar e formatar o CSV de criptomoedas para o padrão do banco de dados.
    """
    print(f"A processar o ficheiro: {nome_arquivo_entrada}...")
    
    # 1. Carregar o CSV original informando o separador correto (;)
    # Utilizamos o pd.read_csv como aprendido para manipular DataFrames
    df_original = pd.read_csv('ETH.csv', sep=';')
    
    # 2. Criar um novo DataFrame vazio para construir a tabela final estruturada
    df_limpo = pd.DataFrame()
    
    # Extraí apenas os primeiros 10 caracteres da string da data (YYYY-MM-DD)
    # Exemplo: de "2026-04-15T00:00:00.000Z" passará a ser "2026-04-15"
    df_limpo['data_registro'] = df_original['timeOpen'].str[:10]
    
    # Pegamos o valor de fechamento do dia para representar o preço da cotação
    df_limpo['preco'] = df_original['close']
    
    # 3. Adicionar as colunas fixas da regra de negócio
    # Preenchemos todas as linhas com a operação 'Fechamento'
    df_limpo['operacao'] = 'Fechamento'
    
    # Adicionamos o ID correspondente à moeda na tabela 'moedas' do MySQL
    df_limpo['id_moeda'] = id_da_moeda
    
    # 4. Salvar o ficheiro final pronto para o MySQL
    # O parâmetro index=False evita que o Pandas crie uma coluna extra com os números das linhas
    df_limpo.to_csv(nome_arquivo_saida, index=False)
    
    print(f"Sucesso! O ficheiro {nome_arquivo_saida} foi gerado e está pronto para o MySQL.\n")

# =====================================================================
# INSTRUÇÕES DE EXECUÇÃO:
# Chama a função para cada um dos teus arquivos.
# IDs: 1 para BTC, 2 para ETH, 3 para BRL
# =====================================================================

# Exemplo para o Bitcoin (Altera 'BTC.csv' para o nome exato do arquivo original)
# preparar_csv_para_mysql(nome_arquivo_entrada='BTC.csv', nome_arquivo_saida='BTC_pronto.csv', id_da_moeda=1)

# É possível descomentar e preencher as linhas abaixo para as outras moedas:
preparar_csv_para_mysql('ETH.csv', 'ETH_pronto.csv', 2)
# preparar_csv_para_mysql('BRL.csv', 'BRL_pronto.csv', 3)