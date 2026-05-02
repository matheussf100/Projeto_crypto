# 📈 Relatório Executivo: Análise Estratégica de Criptomoedas e Moeda Fiduciária

## 1. O que é este projeto?
Este projeto analisa o comportamento histórico de três moedas diferentes: o **Bitcoin (BTC)** e o **Ethereum (ETH)**, que são criptomoedas altamente voláteis, e o **Real Brasileiro (BRL)**, a nossa moeda do dia a dia. 

O objetivo não é apenas mostrar números, mas utilizar a Análise de Dados para encontrar padrões de comportamento, entender o quão estáveis (ou instáveis) essas moedas são e identificar oportunidades de mercado.

## 2. As 5 Perguntas que o nosso Banco de Dados responde
Para entender o mercado, criamos um sistema que processa milhares de dados e responde a 5 perguntas estratégicas:

* **1. Nossos dados são confiáveis? (Volume de Dados)**
Antes de qualquer análise, o sistema conta quantos dias de histórico temos para cada moeda. Isso garante que não estamos tomando decisões baseadas em informações incompletas.

* **2. Quando ocorreram as melhores oportunidades? (Fundo de Mercado)**
O sistema varre a história do Bitcoin e identifica exatamente em quais dias ele esteve mais barato (por exemplo, abaixo da marca psicológica dos 100 mil reais). Para um investidor, saber quando a moeda atinge esses "fundos" ajuda a planejar o melhor momento para comprar.

* **3. Qual é o valor "normal" de cada moeda? (Preço Médio)**
Comparamos o preço médio histórico do BTC, ETH e BRL lado a lado. Isso nos dá uma visão realista de quanto cada ativo costuma valer no dia a dia, ajudando a não criar falsas expectativas.

* **4. Qual foi o limite máximo alcançado? (Teto Histórico / All-Time High)**
O nosso sistema encontra o preço mais alto que cada moeda já atingiu em toda a sua história. O teto histórico é fundamental para o negócio, pois serve como uma meta: se a moeda já chegou àquele valor uma vez, os investidores usam esse número para calcular o potencial máximo de lucro no futuro.

* **5. Como está o nosso dinheiro hoje? (Tendência Recente)**
O mercado muda muito rápido. Por isso, isolamos os dados dos últimos 5 dias do Real Brasileiro. Isso serve para decisões imediatas: se a nossa moeda local está perdendo valor de forma acelerada nesta semana, pode ser o momento ideal para proteger o patrimônio em criptomoedas.

## 3. Entendendo o Comportamento e o Risco dos Preços
Além das perguntas diretas, nossa inteligência artificial analisou a "personalidade" dos preços através da estatística matemática:

* **Dias "Fora da Curva" (Análise de Outliers):** 
Calculamos matematicamente qual é a faixa de preço considerada "normal"[cite: 6]. Tudo o que foge dessa faixa é chamado de *Outlier*. Se identificarmos muitos *outliers* superiores, significa que a moeda teve picos de valorização explosivos e inesperados (eventos raros que geram muito lucro, mas trazem muito risco)[cite: 6].

* **O Nível de Surpresa do Mercado (Assimetria e Curtose):**
Nossa análise classificou o formato do mercado[cite: 9]:
  * Se o resultado for **Leptocúrtico**, significa que o preço passa a maior parte do tempo "parado" no valor médio, mas quando se move, dá saltos gigantescos[cite: 9].
  * Se for **Platicúrtico**, significa que não há um valor previsível: o preço se espalha por vários valores diferentes, tornando a moeda mais instável no dia a dia[cite: 9].
  * Se for **Mesocúrtico**, a moeda é mais calma, previsível e com poucas surpresas, como se espera de moedas tradicionais[cite: 9].

## Conclusão
Com essa infraestrutura de dados pronta, qualquer gestor ou investidor pode olhar para o histórico de milhões de transações e, em poucos segundos, saber exatamente a tendência atual, o limite de lucro esperado e o nível de risco associado a cada uma dessas três moedas.