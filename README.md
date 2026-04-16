# Projeto ETL com Python

Este projeto foi desenvolvido para praticar o processo de **ETL (Extração, Transformação e Carregamento)** utilizando Python.

O objetivo principal é demonstrar, de forma prática, como os dados podem ser lidos de uma fonte, tratados e exportados novamente já transformados.

---

## Objetivo do projeto

Ler um arquivo CSV com dados de usuários, gerar mensagens personalizadas para cada registro e salvar o resultado em um novo arquivo CSV.

---

## Fluxo ETL aplicado

### 1. Extração
Os dados são extraídos do arquivo:

`data/usuarios.csv`

### 2. Transformação
Durante essa etapa, o projeto gera uma mensagem personalizada para cada usuário com base nas informações disponíveis.

### 3. Carregamento
Após a transformação, os dados são salvos em um novo arquivo:

`data/usuarios_com_mensagens.csv`

---

## Estrutura do projeto

```bash
etl-python-lab/
│
├── data/
│   └── usuarios.csv
│
├── src/
│   └── main.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Tecnologias utilizadas

- Python
- Pandas

---

## Como executar o projeto

### 1. Clone este repositório

```bash
git clone <URL_DO_SEU_REPOSITORIO>
```

### 2. Acesse a pasta do projeto

```bash
cd etl-python-lab
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o projeto

```bash
python src/main.py
```

---

## Exemplo de entrada

Arquivo `usuarios.csv`:

```csv
id,nome,conta,cartao
1,Ana,12345-6,5489-XXXX
2,Bruno,98765-4,4532-XXXX
```

---

## Exemplo de saída

Arquivo `usuarios_com_mensagens.csv`:

```csv
id,nome,conta,cartao,mensagem
1,Ana,12345-6,5489-XXXX,"Olá, Ana! Sua conta 12345-6 e seu cartão 5489-XXXX foram processados com sucesso. Aproveite as soluções digitais disponíveis para facilitar sua rotina financeira."
2,Bruno,98765-4,4532-XXXX,"Olá, Bruno! Sua conta 98765-4 e seu cartão 4532-XXXX foram processados com sucesso. Aproveite as soluções digitais disponíveis para facilitar sua rotina financeira."
```

---

## Aprendizados aplicados

Este projeto reforça conceitos importantes de Ciência de Dados e Engenharia de Dados, como:

- Leitura de arquivos CSV
- Validação de colunas
- Manipulação de dados com Pandas
- Geração de novas informações a partir de dados existentes
- Exportação de resultados processados
- Organização de projeto em estrutura simples e clara

---

## Possíveis melhorias futuras

- Ler dados de uma API
- Ler arquivos Excel
- Gerar mensagens com IA
- Salvar resultados em banco de dados
- Criar interface com Streamlit

---

## Autor

Projeto desenvolvido para fins de estudo e portfólio em Python e Ciência de Dados.
