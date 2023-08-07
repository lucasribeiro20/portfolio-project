import dash
import pandas as pd
from dash import dcc
from dash import html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

# Exemplo de dados no DataFrame
data = {
    'mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai'],
    'criptomoeda': ['Bitcoin', 'Bitcoin', 'Ethereum', 'Ethereum', 'Ripple'],
    'valor': [5000, 6000, 5500, 5800, 6200]
}

df = pd.DataFrame(data)

# Criar o aplicativo Dash
app = dash.Dash(__name__)

# Definir o layout da interface gráfica
app.layout = html.Div([
    html.H1("Dashboard de Investimentos"),
    
    # Dropdown para selecionar a criptomoeda
    dcc.Dropdown(
        id='dropdown-criptomoeda',
        options=[{'label': cripto, 'value': cripto} for cripto in df['criptomoeda'].unique()],
        value=df['criptomoeda'].unique()[0]
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
    df_filtrado = df[df['criptomoeda'] == criptomoeda_selecionada]
    fig = go.Figure()

    for criptomoeda, grupo in df_filtrado.groupby('criptomoeda'):
        fig.add_trace(go.Bar(
            x=grupo['mes'],
            y=grupo['valor'],
            name=criptomoeda
        ))

    fig.update_layout(title=f'Valores de {criptomoeda_selecionada} por Mês',
                      xaxis_title='Mês',
                      yaxis_title='Valor (R$)')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)