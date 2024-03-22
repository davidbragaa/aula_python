import pandas as pd
import streamlit as st
import numpy as np

# Lendo o arquivo CSV
df = pd.read_csv("files/exemplo_vendas.csv")

df['% Comissão'] = [f'{comissao / valor_venda * 100:.2f}'
                    for comissao, valor_venda in zip(df['Comissao'], df['Valor Venda'])]

st.header('Acompanhamento de Vendas', divider='rainbow')
st.header('Bem vindo ao seu novo site de analise de Vendas :blue[cool] :sunglasses:', divider='rainbow')

# Dados dos vendedores na tabela
vendedores_unicos = df["Vendedor"].unique()
vendedores_unicos.sort()

categoria = df["Categoria"].unique()
categoria.sort()

# Menu lateral
with st.sidebar:
    st.image('files/gotech.png')
    st.subheader("Menu")

    # Selectbox para uma única seleção e multiselect para várias seleções
    with st.form("Filtro formulario"):
        option1 = st.multiselect('Selecione o Vendedor', vendedores_unicos)
        option2 = st.multiselect('Selecione uma Categoria', categoria)
        submit_button = st.form_submit_button(label='Enviar')

# Aplicar filtros após o envio do formulário
df = df[(df["Vendedor"].isin(option1))]
df = df[(df["Categoria"].isin( option2))]



# Quantidade de colunas e sua dimensão
col1, col2 = st.columns([30, 70])

# col1
with col1:
   st.header("Categoria")
   chart_data = df.set_index('Categoria')
   st.bar_chart(chart_data['Quantidade'])
   
# col2
with col2:
   st.header("Valor")
   if not df.empty:
       chart_data = pd.DataFrame(np.random.randn(20, 1), columns=["a"])
       st.line_chart(chart_data)
   else:
       st.write("Nenhum dado disponível para exibir o gráfico de linhas.")

st.table(df)
