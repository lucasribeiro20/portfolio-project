import pandas as pd

data_path = ('01__carregamento_de_banco\dados_tratados\%s')

# Lendo os dados
database_criptomoedas = pd.read_excel(
    data_path % 'Investimentos Database - PowerBI.xlsx', sheet_name='Criptomoedas')

ultima_data = database_criptomoedas.groupby('Criptomoedas', as_index=False)['Data'].last()
ultima_data = ultima_data.copy()[ultima_data['Criptomoedas']!='Ethereum POW']

ultimo_valor = database_criptomoedas.groupby('Criptomoedas', as_index=False)['value'].last()
ultimo_valor = ultimo_valor.copy()[ultimo_valor['Criptomoedas']!='Ethereum POW']

target_balancemanto = {
    'Bitcoin': 1/2,
    'Ethereum': 1/4,
    'Cardano': 1/12,
    'EOS': 1/12,
    'Litecoin': 1/12,
    'Real': 0}

valor_adicionado = pd.DataFrame({
    'Criptomoedas': ['Real'], 'value': [float(input("Aporte de cripto: "))]})
ultimo_valor = pd.concat([ultimo_valor, valor_adicionado])

ultimo_valor['share_atual'] = ultimo_valor['value']/ultimo_valor['value'].sum()

# Calcular o valor total do portfólio
total_portfolio_value = ultimo_valor['value'].sum()

# Calcular a quantidade alvo de cada moeda
for crypto, target_share in target_balancemanto.items():
    target_value = total_portfolio_value * target_share
    current_value = ultimo_valor[ultimo_valor['Criptomoedas'] == crypto]['value'].values[0]
    buy_value = target_value - current_value
    if buy_value > 0:
        print(f'Comprar R$ {buy_value:.2f} de {crypto}')