import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def treinar_modelo(X_encoded, y):
    """Treina o Random Forest e calcula o relatório detalhado de acertos e importâncias."""
    # Divisão 80% Treino e 20% Teste
    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y, test_size=0.2, random_state=42
    )
    
    # Treinamento
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    
    # Previsão
    predicoes = modelo.predict(X_test)
    acuracia = accuracy_score(y_test, predicoes)
    porcentagem = acuracia * 100
    
    # Importância das Variáveis
    importancias = pd.DataFrame({
        'Informação': X_encoded.columns,
        'Importancia': modelo.feature_importances_ * 100
    }).sort_values(by='Importancia', ascending=True).tail(8)
    
    # Detalhamento de Acertos e Erros por Categoria
    labels = sorted(list(y.unique()))
    cm = confusion_matrix(y_test, predicoes, labels=labels)
    
    resumo_categorias = []
    for i, label in enumerate(labels):
        total_real = cm[i].sum()
        acertos = cm[i][i]
        erros = total_real - acertos
        taxa = (acertos / total_real * 100) if total_real > 0 else 0
        resumo_categorias.append({
            "Opção / Categoria": str(label),
            "Total na Prova": total_real,
            "Acertos Diretos": acertos,
            "Erros de Chute": erros,
            "Acurácia da Categoria": f"{taxa:.1f}%"
        })
        
    df_resumo = pd.DataFrame(resumo_categorias)
    
    return {
        "porcentagem": porcentagem,
        "len_test": len(y_test),
        "len_train": len(y_train),
        "importancias": importancias,
        "df_resumo": df_resumo
    }

def calcular_correlacao(df):
    """Calcula a matriz de correlação transformando dados categóricos em números temporários."""
    df_numerico = df.apply(lambda col: pd.factorize(col)[0])
    return df_numerico.corr()