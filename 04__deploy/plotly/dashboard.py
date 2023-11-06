import dash
import pandas as pd
from dash import dcc
from dash import html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

data_path = ('01__carregamento_de_banco\dados_tratados\%s')

# Lendo os dados
database_criptomoedas = pd.read_excel(
    data_path % 'Investimentos Database - PowerBI.xlsx', sheet_name='Criptomoedas')

# Criar o aplicativo Dash
app = dash.Dash(__name__)

# Definir o layout da interface gráfica
app.layout = html.Div([
    html.H1("Dashboard de Investimentos"),
    
    # Dropdown para selecionar a criptomoeda
    dcc.Dropdown(
        id='dropdown-criptomoeda',
        options=[{'label': cripto, 'value': cripto} for cripto in database_criptomoedas[
            'Criptomoedas'].unique()],
        value=database_criptomoedas['Criptomoedas'].unique()[0]
    ),
    
    # Gráfico de barras agrupadas
    dcc.Graph(id='grafico-investimentos')
])

# Função para atualizar o gráfico com base na criptomoeda selecionada
@app.callback(
    Output('grafico-investimentos', 'figure'),
    [Input('dropdown-criptomoeda', 'value')]
)
def atualizar_grafico(criptomoeda_selecionada):
    df_filtrado = database_criptomoedas.copy()[
        database_criptomoedas['Criptomoedas'] == criptomoeda_selecionada]
    fig = go.Figure()

    for criptomoeda, grupo in df_filtrado.groupby('Criptomoedas'):
        fig.add_trace(go.Bar(
            x=grupo['Data'],
            y=grupo['value'],
            name=criptomoeda
        ))

    fig.update_layout(title=f'Valores de {criptomoeda_selecionada} por Mês',
                      xaxis_title='Mês',
                      yaxis_title='Valor (R$)')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)