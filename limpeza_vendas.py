import pandas as pd

def limpar_dados_vendas(caminho_entrada, caminho_saida):
    """Função para limpar e tratar dados de vendas."""
    
    # Leitura do arquivo CSV
    df = pd.read_csv(caminho_entrada)

    # Conversão da coluna de data
    df['Data_Venda'] = pd.to_datetime(df['Data_Venda'], format='%Y-%m-%d')

    # Limpeza da coluna de Preço
    df['Preço'] = df['Preço'].str.replace("'", '').astype('float64')

    # Preenchimento de valores nulos com valores padrão
    df['Produto'].fillna('Produto B', inplace=True)
    df['Categoria'].fillna('Categoria 3', inplace=True)
    df['Data_Venda'].fillna('2023-12-31', inplace=True)
    df['Vendedor'].fillna('Vendedor 1', inplace=True)

    # Cálculo da coluna Total_Vendas
    df['Total_Vendas'] = df['Quantidade'] * df['Preço']

    # Renomear colunas
    df.columns = ['ID','Produto', 'Categoria', 'Preco', 'Quantidade', 'Data_Venda', 'Vendedor', 'Total_Vendas']

    # Exportar o arquivo limpo
    df.to_csv(caminho_saida, index=False)
