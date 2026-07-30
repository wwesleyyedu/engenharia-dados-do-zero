# Engenharia de Dados do Zero

## Visão geral

Este projeto é um laboratório de Engenharia de Dados construído para demonstrar um pipeline completo de ETL utilizando Python e SQLite. Ele inclui extração de dados a partir de CSV, transformação de dados com cálculo de métricas e carregamento em banco de dados local.

## Tecnologias

- Python 3.14
- pandas
- SQLite
- Jupyter Notebook
- Git

## Estrutura do projeto

- `data/`
  - `vendas.csv` — dataset de vendas usadas no pipeline
- `src/`
  - `extract.py` — extração de dados
  - `transform.py` — transformação de dados
  - `load.py` — carregamento em banco SQLite
  - `logger.py` — logging simples de execução
  - `main.py` — ponto de entrada do pipeline
- `notebooks/`
  - `analise.ipynb` — análise exploratória e estudo do dataset
- `sql/`
  - `consultas.sql` — exemplos de consultas SQL para análise dos dados
- `vendas.db` — banco de dados SQLite gerado pelo pipeline

## Como executar

1. Ative seu ambiente virtual:

```powershell
cd C:\Users\wesle\engenharia-dados\engenharia-dados-do-zero
.venv\Scripts\Activate.ps1
```

2. Instale dependências:

```powershell
pip install -r requirements.txt
```

3. Execute o pipeline:

```powershell
python src\main.py
```

## Resultado esperado

Após a execução, o pipeline deve:

- carregar `data/vendas.csv`
- calcular `valor_total` para cada registro
- gravar a tabela `vendas` em `vendas.db`
- exibir logs de progresso no terminal

## Estrutura do pipeline

- `extract.py`: lê o CSV e retorna um DataFrame pandas
- `transform.py`: aplica cálculos e limpa dados
- `load.py`: grava o DataFrame no banco SQLite
- `main.py`: orquestra as etapas e resolve caminhos relativos

## Observações

- O pipeline assume que o arquivo `data/vendas.csv` existe.
- O banco `vendas.db` é criado no diretório do projeto.
- Para usar o notebook `analise.ipynb`, abra-o no Jupyter a partir da raiz do projeto.

## Contato

Este projeto foi desenvolvido por um engenheiro de dados em formação como exemplo de pipeline ETL básico.
