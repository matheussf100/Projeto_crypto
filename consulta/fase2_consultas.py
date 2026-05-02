import mysql.connector

# =====================================================================
# 1. FUNÇÃO DE CONEXÃO E EXECUÇÃO
# =====================================================================
def obter_dados_do_banco(query):
    """
    Função base para conectar ao banco de dados MySQL local, 
    executar a query solicitada e retornar as linhas de dados.
    """
    try:
        conexao = mysql.connector.connect(
            host="localhost", user="root", password="", database="projeto_crypto"
        )
        cursor = conexao.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

# =====================================================================
# 2. AS 5 CONSULTAS ESTRATÉGICAS DOCUMENTADAS (DQL)
# =====================================================================

# -- Estratégia: Realiza uma auditoria de qualidade e volume na base de dados.
# -- Garante que temos uma amostra confiável e balanceada para cada ativo antes da análise.
query_1 = """
SELECT m.nome, COUNT(c.id_cotacao) as total_registos
FROM moedas m
JOIN cotacoes c ON m.id_moeda = c.id_moeda
GROUP BY m.nome;
"""

# -- Estratégia: Identifica fundos de mercado e oportunidades de risco/retorno.
# -- Mapeia os dias exatos em que o Bitcoin operou abaixo de um suporte psicológico (100k).
query_2 = """
SELECT data_registro, preco, operacao 
FROM cotacoes 
WHERE id_moeda = 1 AND preco < 100000;
"""

# -- Estratégia: Cria um Resumo Executivo comparando o desempenho médio dos ativos.
# -- Cruza tabelas para mostrar o preço médio histórico, avaliando o comportamento geral.
query_3 = """
SELECT m.sigla, AVG(c.preco) as preco_medio
FROM moedas m
JOIN cotacoes c ON m.id_moeda = c.id_moeda
GROUP BY m.sigla;
"""

# -- Estratégia: Descobre o 'All-Time High' (Valor Máximo Histórico) de CADA moeda.
# -- Serve como a principal meta fundamental para os investidores calcularem rentabilidade futura.
query_4 = """
SELECT m.sigla, MAX(c.preco) as preco_maximo
FROM moedas m
JOIN cotacoes c ON m.id_moeda = c.id_moeda
GROUP BY m.sigla;
"""

# -- Estratégia: Cria um panorama atualizado focando na tendência mais recente.
# -- Prioriza a volatilidade dos últimos 5 dias do Real (BRL) para decisões de câmbio de curto prazo.
query_5 = """
SELECT data_registro, preco 
FROM cotacoes 
WHERE id_moeda = 3
ORDER BY data_registro DESC
LIMIT 5;
"""

# =====================================================================
# 3. EXECUÇÃO: MENU INTERATIVO
# =====================================================================

def exibir_resultados(dados):
    """Função auxiliar para imprimir os dados no terminal de forma limpa."""
    if dados:
        for linha in dados:
            print(linha)
    else:
        print("-> Nenhum dado encontrado ou erro na consulta.")

# Loop infinito para manter o menu funcionando até o utilizador decidir sair
while True:
    print("\n" + "="*55)
    print("        PAINEL ESTRATÉGICO DE CRIPTOMOEDAS")
    print("="*55)
    print("1 - Auditoria e Volume (Contagem de cotações)")
    print("2 - Oportunidade de Compra (BTC abaixo de 100k)")
    print("3 - Resumo Executivo (Preço Médio por Moeda)")
    print("4 - Análise de Topo (All-Time High de todas as moedas)")
    print("5 - Tendência Recente (Últimos 5 dias do BRL)")
    print("0 - Sair do programa")
    print("="*55)
    
    escolha = input("Digite o número da consulta que deseja visualizar: ")
    
    if escolha == '1':
        print("\n--- 1. Auditoria e Volume ---")
        exibir_resultados(obter_dados_do_banco(query_1))
        
    elif escolha == '2':
        print("\n--- 2. Oportunidade de Compra (BTC) ---")
        exibir_resultados(obter_dados_do_banco(query_2))
        
    elif escolha == '3':
        print("\n--- 3. Resumo Executivo Geral ---")
        exibir_resultados(obter_dados_do_banco(query_3))
        
    elif escolha == '4':
        print("\n--- 4. Teto Histórico das Moedas ---")
        exibir_resultados(obter_dados_do_banco(query_4))
        
    elif escolha == '5':
        print("\n--- 5. Tendência Recente (BRL) ---")
        exibir_resultados(obter_dados_do_banco(query_5))
        
    elif escolha == '0':
        print("\nFase 2 concluída e documentada! Encerrando o programa.")
        break
        
    else:
        print("\nOpção inválida! Por favor, digite um número de 0 a 5.")