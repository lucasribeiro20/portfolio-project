import pandas as pd
import plotly.graph_objects as go

data_path = ('01__carregamento_de_banco\dados_tratados\%s')

# Lendo os dados
database_criptomoedas = pd.read_excel(
    data_path % 'Investimentos Database - PowerBI.xlsx', sheet_name='Criptomoedas')

database_acoes = pd.read_excel(
    data_path % 'Investimentos Database - PowerBI.xlsx', sheet_name='Ações')

database_fi = pd.read_excel(
    data_path % 'Investimentos Database - PowerBI.xlsx', sheet_name='Fundos Imobiliários')

database_div_acoes = pd.read_excel(
    data_path % 'Investimentos Database - PowerBI.xlsx', sheet_name='Ações_Dividendos-Juros')

database_div_fi = pd.read_excel(
    data_path % 'Investimentos Database - PowerBI.xlsx', sheet_name='Fundos Imobiliários_Dividendos')

database_caixinhas = pd.read_excel(
    data_path % 'Investimentos Database - PowerBI.xlsx', sheet_name='Caixinhas Nubank')

database_de_para = pd.read_excel(
    data_path % 'Investimentos Database - PowerBI.xlsx', sheet_name='De-Para')


# Criar o gráfico de barras agrupadas
fig = go.Figure()

for criptomoeda, grupo in database_criptomoedas.groupby('Criptomoedas'):
    fig.add_trace(go.Bar(
        x=grupo['Data'],
        y=grupo['value'],
        name=criptomoeda
    ))

# Adicionar título e rótulos aos eixos
fig.update_layout(title='Valores de Criptomoedas por Mês',
                  xaxis_title='Mês',
                  yaxis_title='Valor (R$)')

# Exibir o gráfico
fig.show()