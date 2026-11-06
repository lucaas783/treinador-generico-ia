import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

from data_processing import carregar_dados, preparar_dados
from logica_algoritmo import treinar_modelo, calcular_correlacao

# Configuração da página
st.set_page_config(page_title="Treinador de IA Genérico", layout="wide")

st.title("Treinador Genérico de IA")
st.write("Carregue sua tabela, escolha o que deseja prever e a IA explicará todo o desempenho de forma simples e visual.")

# 1. Upload do arquivo
arquivo = st.file_uploader("Carregue seu arquivo de dados", type=["csv", "xlsx", "xls"])

if arquivo is not None:
    df_original = carregar_dados(arquivo)
    
    # 2. Seleção das colunas
    colunas_selecionadas = st.multiselect(
        "Selecione as colunas que deseja utilizar na análise (mínimo 2):",
        options=df_original.columns.tolist(),
        default=df_original.columns.tolist()
    )

    if len(colunas_selecionadas) < 2:
        st.warning("⚠️ Por favor, selecione pelo menos 2 colunas para prosseguir com a visualização e o treinamento.")
    else:
        df = df_original[colunas_selecionadas]
        
        st.subheader("1. Prévia dos Seus Dados")
        st.dataframe(df.head(4), use_container_width=True)
        
        # 3. Escolha do Alvo Y
        coluna_alvo = st.selectbox("Selecione a coluna que a IA deve aprender a prever (Coluna Alvo Y):", colunas_selecionadas)
        
        # 4. Botão de Execução
        if st.button("Treinar IA e Gerar Relatório", type="primary"):
            with st.spinner("Treinando a IA e preparando o relatório visual..."):
                
                # Chamada das funções dos módulos
                X_encoded, y, df_limpo = preparar_dados(df_original, colunas_selecionadas, coluna_alvo)
                resultados = treinar_modelo(X_encoded, y)
                
                st.divider()
                st.header("Relatório Intuitivo de Desempenho")

                st.info("""
                **Algoritmo Utilizado: Floresta Aleatória (Random Forest)**  
                Este modelo funciona como uma **votação em equipe**: a IA cria 100 'árvores de decisão' (pequenos robôs especialistas). 
                Cada árvore analisa os dados sob um ponto de vista diferente e dá o seu palpite. A resposta final exibida aqui é decidida pelo **voto da maioria**.
                """)
                
                # Métricas
                col1, col2, col3 = st.columns(3)
                col1.metric(label="Taxa Geral de Acerto", value=f"{resultados['porcentagem']:.1f}%")
                col2.metric(label="Casos Usados no Teste", value=f"{resultados['len_test']} respostas")
                col3.metric(label="Casos Usados no Estudo", value=f"{resultados['len_train']} respostas")
                
                # Diagnóstico
                porcentagem = resultados['porcentagem']
                if porcentagem >= 80:
                    st.success(f"**Diagnóstico:** Excelente desempenho! Em cada 100 casos novos, a IA acerta em média **{int(porcentagem)}**. Os dados continham ótimas pistas.")
                elif porcentagem >= 50:
                    st.warning(f"**Diagnóstico:** Desempenho moderado. Em cada 100 casos novos, a IA acerta em média **{int(porcentagem)}**. Algumas respostas foram difíceis de prever com os dados atuais.")
                else:
                    st.error(f"**Diagnóstico:** Desempenho baixo. Em cada 100 casos novos, a IA acerta apenas **{int(porcentagem)}**. Isso acontece quando as colunas de entrada não têm relação direta com o que você quer prever.")
                    
                st.divider()
                
                # Gráfico de Importâncias
                st.subheader("Quais colunas mais ajudaram a IA a decidir?")
                st.write("Este gráfico mostra quanto peso cada informação teve para a IA formular as respostas:")
                
                fig, ax = plt.subplots(figsize=(8, 3.5))
                importancias = resultados['importancias']
                ax.barh(importancias['Informação'], importancias['Importancia'], color='#2b5c8f')
                ax.set_xlabel('Nível de Importância (%)')
                ax.set_title('Rank de Pistas Mais Relevantes')
                st.pyplot(fig)
                
                st.caption("**Como ler o gráfico:** Quanto mais longa a barra azul, mais a IA dependeu dessa informação para tentar acertar o resultado.")
                
                st.divider()

                # Matriz de Correlação
                st.subheader("Matriz de Correlação Visual")
                matriz_correlacao = calcular_correlacao(df_limpo)

                fig, ax = plt.subplots(figsize=(6, 4))
                sns.heatmap(matriz_correlacao, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
                st.pyplot(fig)

                st.caption("**Como ler o gráfico:** Valores próximos de +1.0 ou -1.0 indicam forte correlação entre as colunas. Valores próximos de 0.0 indicam ausência de relação.")
                
                # Tabela de Categorias
                st.subheader("Detalhamento dos Acertos e Erros por Categoria")
                st.dataframe(resultados['df_resumo'], use_container_width=True)
                
                st.caption("**Legenda da Tabela:**")
                st.caption("- **Total na Prova:** Quantas vezes essa opção realmente apareceu no teste final.")
                st.caption("- **Acertos Diretos:** Quantas vezes a IA chutou exatamente essa opção e acertou.")
                st.caption("- **Erros de Chute:** Quantas vezes a IA errou ao tentar prever essa opção.")
                
                st.divider()
                
                # Guia Educativo
                with st.expander("Não entendeu? Veja abaixo como funcionou o processo de aprendizado da IA"):
                    st.markdown("""
                    1. **O Treinamento:** A IA separou 80% do seu arquivo para 'estudar' e descobrir padrões entre as colunas.
                    2. **O Teste:** Os outros 20% ficaram escondidos. A IA tentou adivinhar a resposta desses casos sem olhar o gabarito.
                    3. **A Nota Final:** A porcentagem de acerto é a nota que a IA tirou nesse teste surpresa.
                    4. **Como melhorar a nota?** Se a taxa de acerto estiver baixa, experimente adicionar colunas com mais detalhes ou coletar mais respostas na planilha.
                    """)