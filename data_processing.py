import pandas as pd

def carregar_dados(arquivo):
    """Carrega arquivos no formato CSV ou Excel."""
    if arquivo.name.endswith('.csv'):
        return pd.read_csv(arquivo)
    else:
        return pd.read_excel(arquivo)

def preparar_dados(df_original, colunas_selecionadas, coluna_alvo):
    """Filtra as colunas escolhidas, remove linhas nulas e trata variáveis de texto."""
    df_filtrado = df_original[colunas_selecionadas]
    df_limpo = df_filtrado.dropna()
    
    y = df_limpo[coluna_alvo]
    X = df_limpo.drop(columns=[coluna_alvo])
    
    # Converter colunas de texto em números (dummy variables)
    X_encoded = pd.get_dummies(X, drop_first=True)
    
    return X_encoded, y, df_limpo