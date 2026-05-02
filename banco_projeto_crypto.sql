-- Criação do banco de dados
CREATE DATABASE projeto_crypto;
USE projeto_crypto;

-- Criação da tabela de moedas (Entidade principal)
CREATE TABLE moedas (
    id_moeda INT PRIMARY KEY,
    sigla VARCHAR(10),
    nome VARCHAR(100)
);

-- Criação da tabela de cotações com Chave Estrangeira
CREATE TABLE cotacoes (
    id_cotacao INT PRIMARY KEY,
    data_registro DATE,
    preco DECIMAL(10, 2),
    operacao VARCHAR(50),
    id_moeda INT,
    FOREIGN KEY (id_moeda) REFERENCES moedas(id_moeda)
);

-- Inserindo os dados fixos das nossas 3 moedas
INSERT INTO moedas (id_moeda, sigla, nome) VALUES
(1, 'BTC', 'Bitcoin'),
(2, 'ETH', 'Ethereum'),
(3, 'BRL', 'Real Brasileiro');

-- 1. Primeiro, apagamos a tabela atual que está vazia
DROP TABLE cotacoes;

-- 2. Recriamos a tabela adicionando o AUTO_INCREMENT à Chave Primária
CREATE TABLE cotacoes (
    id_cotacao INT PRIMARY KEY AUTO_INCREMENT,
    data_registro DATE,
    preco DECIMAL(10, 2),
    operacao VARCHAR(50),
    id_moeda INT,
    FOREIGN KEY (id_moeda) REFERENCES moedas(id_moeda)
);