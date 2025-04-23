# Limpeza de Dados de Vendas

Este projeto contém um script Python para realizar a limpeza de dados de um arquivo CSV contendo informações de vendas.

## Estrutura

- `data/`: Contém o arquivo original de vendas
- `output/`: Arquivo tratado e exportado
- `limpeza_vendas.py`: Script de limpeza
- `README.md`: Este arquivo de documentação

## Como usar

1. Coloque o arquivo `vendas_ficticias.csv` na pasta `data/`.
2. Rode o script `limpeza_vendas.py`, chamando a função:

```python
from limpeza_vendas import limpar_dados_vendas

limpar_dados_vendas('data/vendas_ficticias.csv', 'output/vendas_ficticias_limpo.csv')
```

3. O arquivo tratado será salvo na pasta `output/`.
