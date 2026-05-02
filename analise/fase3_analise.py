import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================================
# 1. FUNÇÃO PRINCIPAL DE ANÁLISE
# =====================================================================
def analisar_estatisticas_moeda(nome_arquivo):
    """
    Função que recebe um arquivo CSV limpo, realiza os cálculos
    estatísticos e agora inclui a interpretação detalhada da Curtose.
    """
    print(f"\n" + "="*60)
    print(f" INICIANDO ANÁLISE ESTATÍSTICA: {nome_arquivo}")
    print("="*60)

    # 1. Carregamento dos dados
    df = pd.read_csv(nome_arquivo)
    dados_preco = df['preco']

    # 2. Resumo Inicial (Describe e Soma)
    print("\n--- Elementos do Describe ---")
    print(dados_preco.describe())
    print(f"\nSoma Total dos Preços Registados: R$ {dados_preco.sum():.2f}")

    # 3. Medidas de Tendência Central e Dispersão
    media = dados_preco.mean()
    mediana = dados_preco.median()
    variancia = np.var(dados_preco, ddof=0) 
    desvio_padrao = np.std(dados_preco, ddof=0) 

    # 4. Medidas de Posicionamento (Quartis e Percentis)
    Q1 = np.percentile(dados_preco, 25)
    Q3 = np.percentile(dados_preco, 75)
    IQR = Q3 - Q1 

    print("\n--- Medidas de Tendência e Posição ---")
    print(f"Média: R$ {media:.2f} | Mediana (Q2): R$ {mediana:.2f}")
    print(f"Desvio Padrão: R$ {desvio_padrao:.2f} | Variância: {variancia:.2f}")
    print(f"Q1: R$ {Q1:.2f} | Q3: R$ {Q3:.2f} | IQR: R$ {IQR:.2f}")

    # 5. Limpeza de Dados e Identificação de Outliers
    limite_superior = Q3 + (1.5 * IQR)
    limite_inferior = Q1 - (1.5 * IQR)

    outliers_superiores = df[df['preco'] > limite_superior]
    outliers_inferiores = df[df['preco'] < abs(limite_inferior)]

    print("\n--- Análise de Outliers (Valores Atípicos) ---")
    print(f"Limite Superior: R$ {limite_superior:.2f} | Limite Inferior: R$ {limite_inferior:.2f}")
    print(f"Encontrados {len(outliers_superiores)} outliers superiores.")
    print(f"Encontrados {len(outliers_inferiores)} outliers inferiores.")

    # =====================================================================
    # NOVIDADE: 6. ASSIMETRIA E CLASSIFICAÇÃO DA CURTOSE
    # =====================================================================
    assimetria = dados_preco.skew()
    # Para a Curtose Real, adicionamos 3 ao valor padrão do Pandas
    curtose_real = dados_preco.kurtosis() + 3

    print("\n--- Formato da Distribuição ---")
    print(f"Assimetria: {assimetria:.4f} (Lateralidade da amostra)")
    print(f"Curtose Real calculada: {curtose_real:.4f}\n")

    # Estrutura de decisão para classificar e explicar a Curtose
    if curtose_real >= 2.5 and curtose_real <= 3.5:
        print("-> Classificação: MESOCÚRTICA")
        print("   Porquê? O valor está entre 2.5 e 3.5. A distribuição é próxima da curva normal.")
        print("   Significado: Os dados estão uniformemente distribuídos no entorno da média. Outliers são menos comuns.")
        
    elif curtose_real < 2.5:
        print("-> Classificação: PLATICÚRTICA")
        print("   Porquê? O valor é menor que 2.5. O pico do gráfico é mais baixo e as caudas são mais finas.")
        print("   Significado: Os dados estão mais dispersos em relação à média. Outliers são comuns.")
        
    else: # Se não for nenhum dos anteriores, será maior que 3.5 (Leptocúrtica)
        print("-> Classificação: LEPTOCÚRTICA")
        print("   Porquê? O valor é maior que 3.5. O pico é mais alto e as caudas são mais grossas.")
        print("   Significado: Os dados estão extremamente concentrados no entorno da média. Outliers são muito comuns nas caudas grossas.")

    # =====================================================================
    # 7. APRESENTAÇÃO EM GRÁFICO (MATPLOTLIB & SEABORN)
    # =====================================================================
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Histograma com Linha de Densidade (KDE)
    sns.histplot(dados_preco, kde=True, ax=axes[0], color='skyblue', edgecolor='black')
    axes[0].axvline(media, color='red', linestyle='--', label=f'Média: {media:.2f}')
    axes[0].axvline(mediana, color='green', linestyle='-', label=f'Mediana: {mediana:.2f}')
    axes[0].set_title(f'Distribuição de Preços - {nome_arquivo}')
    axes[0].set_xlabel('Preço (R$)')
    axes[0].set_ylabel('Frequência / Densidade')
    axes[0].legend()

    # Boxplot (Diagrama de Caixa)
    sns.boxplot(y=dados_preco, ax=axes[1], color='lightgray')
    axes[1].set_title('Boxplot (Dispersão e Outliers)')
    axes[1].set_ylabel('Preço (R$)')

    plt.tight_layout()
    plt.show()

# =====================================================================
# 3. EXECUÇÃO
# =====================================================================
# Podes testar com o arquivo BRL_pronto.csv, BTC_pronto.csv ou ETH_pronto.csv
analisar_estatisticas_moeda('C:\\Users\\Matheus\\Documents\\Projeto_crypto\\limpeza\\BRL_pronto.csv')