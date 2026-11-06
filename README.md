# 🤖 Treinador Genérico de IA (AutoML & Data Storytelling)

Uma ferramenta web interativa e descomplicada que transforma qualquer tabela do Excel ou CSV em um modelo de Inteligência Artificial, gerando relatórios em linguagem simples sem que o usuário precise entender de programação ou estatística.

Link da ferramenta online para uso: <a href="https://treinadorgenericoia.streamlit.app/">Clique aqui<a/>

---

## 📌 O que o projeto faz?

Imagine ter uma planilha com dados de clientes, alunos ou vendas e querer adivinhar um resultado futuro (por exemplo: *"Quem vai cancelar a assinatura?"*, *"Quem vai praticar qual esporte?"* ou *"Quem tem chance de comprar um produto?"*).

Normalmente, isso exige criar códigos complexos de Ciência de Dados. Esta aplicação automatiza todo esse processo:
1. Você envia sua planilha (`.csv` ou `.xlsx`).
2. Escolhe quais colunas deseja analisar e a resposta que quer prever.
3. A IA treina um modelo preditivo automaticamente e entrega um **boletim explicativo completo**, mostrando as taxas de acerto, quais dados influenciaram a decisão e onde o modelo acertou ou errou.

---

## 💡 Por que este projeto é útil no mundo real?

Muitas empresas possuem toneladas de dados guardados em planilhas, mas não contam com cientistas de dados dedicados para analisá-los. Esta ferramenta resolve dois grandes problemas:

1. **Prototipagem Rápida (AutoML):** Permite que qualquer pessoa teste se os dados de uma planilha têm valor preditivo real em questão de segundos.
2. **Data Storytelling (Tradução para Leigos):** Em vez de exibir relatórios técnicos cheios de termos difíceis (como *Recall*, *F1-Score* ou *Matriz de Confusão*), a ferramenta traduz tudo para frases claras (ex: *"Em cada 100 casos novos, a IA acerta em média X"*).

### 🎯 Exemplos de uso prático:
* **Vendas & Marketing:** Identificar o perfil de cliente com maior chance de fechar um contrato.
* **Recursos Humanos:** Entender quais fatores aumentam a chance de um funcionário pedir demissão.
* **Educação:** Prever o risco de evasão escolar com base no perfil e comportamento do estudante.
* **Atendimento:** Antecipar o tipo de problema que um cliente trará no suporte.

---

## ⚙️ Funcionalidades principais

- 📁 **Suporte Flexível a Arquivos:** Aceita tabelas em formato CSV e Excel.
- 🎯 **Seleção Personalizada:** Escolha livre de quais colunas usar e qual será o alvo ($Y$) da previsão.
- 🌲 **Algoritmo Random Forest (Floresta Aleatória):** Modelo robusto baseado no voto da maioria de 100 especialistas virtuais.
- 📊 **Rank de Relevância das Pistas:** Gráfico visual mostrando quais colunas mais ajudaram a IA a tomar decisões.
- 🔗 **Matriz de Correlação Visual:** Mapa de calor simples para identificar quais informações sobem ou descem juntas.
- 📋 **Tabela de Acertos e Erros:** Detalhamento transparente do desempenho da IA em cada categoria.

---

## 📁 Estrutura do Código

O projeto foi construído seguindo boas práticas de **modularização**, separando o código em três partes com responsabilidades bem definidas:

```text
treinador_generico_ia/
│
├── data_processing.py    # Leitura de planilhas e tratamento automático de dados
├── logica_algoritmo.py          # Treinamento do modelo de IA e cálculo de estatísticas
└── app.py                # Interface gráfica e telas interativas (Streamlit)
