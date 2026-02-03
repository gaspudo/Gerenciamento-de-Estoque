# 📦 Sistema de Gestão de Estoque em Python
Este é um projeto desenvolvido para consolidar fundamentos de lógica de programação em Python, focado em manipulação de estruturas de dados (listas e tuplas), controle de fluxo e tratamento de exceções.

## 🚀 Funcionalidades
### Entrada Dinâmica: 
Cadastro de produtos e preços via terminal com normalização de strings.

### Tratamento de Erros: 
Validação de tipos de dados para evitar quebras por entradas inválidas (ex: letras no campo de preço).

### Processamento de Dados:

Cálculo automático de média aritmética de preços.

Identificação do produto de maior e menor valor.

Ordenação dinâmica da lista de produtos por preço.

### Modularidade: 
Código estruturado em funções e protegido pelo bloco if __name__ == "__main__": para permitir importação modular.

## 🛠️ Tecnologias Utilizadas
Python 3.x

### Estruturas: 
list, tuple, lambda functions para ordenação.

## 📂 Como rodar o projeto
Certifique-se de ter o Python instalado.

Clone o repositório:

Bash
git clone https://github.com/gaspudo/Gerenciamento-de-Estoque.git
Navegue até a pasta e execute:

Bash
python gerenciamento-estoque.py

## 🧠 O que eu aprendi neste projeto
### Neste desafio, foquei em resolver problemas comuns de quem está começando:

Escopo de Variáveis: Aprendi a importância de não depender de variáveis globais e como passar argumentos entre funções.

Eficiência (Big O): Entendi que realizar operações pesadas (como .sort()) dentro de laços de repetição é uma falha grave de performance.

Robustez: Implementação de try-except para garantir que o software não feche inesperadamente por erro do usuário.
