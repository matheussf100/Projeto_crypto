# 📊 Projeto Final: Big Data Science - Análise de Criptomoedas

## 📝 Descrição do Projeto
Este projeto consiste numa Análise Exploratória de Dados (EDA) e Modelagem Relacional focada no mercado financeiro, comparando o comportamento histórico de duas das maiores criptomoedas (Bitcoin e Ethereum) com uma moeda fiduciária (Real Brasileiro). 

O projeto está estruturado em três grandes fases, abrangendo desde a criação e modelagem de um banco de dados relacional até à extração de insights estatísticos avançados utilizando Python.

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Banco de Dados:** MySQL (via XAMPP)
* **Linguagem:** Python 3.x
* **Manipulação de Dados:** Pandas, NumPy
* **Visualização de Dados:** Matplotlib, Seaborn
* **Integração:** mysql-connector-python

## 🗂️ Estrutura do Projeto e Fases

### Fase 1: Modelagem e Banco de Dados (SQL)
Criação do banco de dados local `projeto_crypto` com integridade referencial.
* **Tabelas:**
  * `moedas`: Tabela dimensional contendo os IDs e siglas (BTC, ETH, BRL).
  * `cotacoes`: Tabela de fatos contendo o histórico de preços, datas e operações, conectada por Chave Estrangeira (Foreign Key).
* **Pré-processamento:** Scripts de limpeza em Python para padronizar ficheiros CSV originais (conversão de separadores `;` para `,` e extração de datas) antes da importação.

### Fase 2: Consultas Estratégicas e DQL (Python + MySQL)
Desenvolvimento do script `fase2_consultas.py`, que atua como uma interface de terminal interativa para consultar o banco de dados. O menu inclui 5 análises de negócios:
1. **Auditoria e Volume:** Contagem total de registos por moeda usando `COUNT` e `GROUP BY`.
2. **Oportunidade de Compra:** Filtro de fundos de mercado do BTC abaixo de 100k usando `WHERE`.
3. **Resumo Executivo:** Cálculo do preço médio por moeda através de junções (`JOIN`).
4. **Análise de Topo:** Identificação do All-Time High (Valor Máximo Histórico) individual dos ativos.
5. **Tendência Recente:** Monitorização da volatilidade de curto prazo do Real Brasileiro (`ORDER BY DESC`).

### Fase 3: Análise Estatística e Visualização Exploratória
Desenvolvimento do script `fase3_analise.py`, que consome os ficheiros CSV para realizar uma análise descritiva profunda:
* **Medidas de Tendência e Dispersão:** Cálculo da Média, Mediana, Variância e Desvio Padrão populacional.
* **Tratamento de Outliers:** Utilização da Amplitude Interquartil (IQR) para calcular limites (Superior e Inferior) e isolar valores atípicos de preço.
* **Análise de Forma:** Avaliação do comportamento da curva de distribuição calculando a Assimetria e classificando matematicamente a Curtose Real (Leptocúrtica, Mesocúrtica ou Platicúrtica).
* **Painel Visual:** Geração de um painel integrado com Subplots contendo um Histograma com estimativa de densidade (KDE) e um Boxplot para evidenciar dispersão e valores extremos.

## 🚀 Como Executar o Projeto

**Pré-requisitos:**
1. Ter o XAMPP instalado e os módulos Apache e MySQL em execução.
2. Ter o Python instalado junto com um Ambiente Virtual (`venv`).
3. Instalar as dependências do ficheiro `requirements.txt` (`pip install pandas numpy matplotlib seaborn mysql-connector-python`).

**Passo a Passo:**
1. Importe a estrutura do banco de dados via PhpMyAdmin e garanta que a tabela `cotacoes` possui a configuração `AUTO_INCREMENT`.
2. Execute o script de consultas estratégicas para validar a conexão com o banco:
   ```bash
   python fase2_consultas.py