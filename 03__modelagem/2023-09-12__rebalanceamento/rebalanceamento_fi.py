import pandas as pd

data_path = ('01__carregamento_de_banco\dados_tratados\%s')

# Lendo os dados
database_fi = pd.read_excel(
    data_path % 'Investimentos Database - PowerBI.xlsx', sheet_name='Fundos Imobiliários')

ultima_data = database_fi.groupby('Fundos Imobiliarios', as_index=False)['Data'].last()

ultimo_valor = database_fi.groupby('Fundos Imobiliarios', as_index=False)['value'].last()

target_balancemanto = {
    'CPTS11': 1/3,
    'KNSC11': 1/3,
    'RBRR11': 1/3,
    'Real': 0}

valor_adicionado = pd.DataFrame({
    'Fundos Imobiliarios': ['Real'], 'value': [float(input("Aporte de FI: "))]})
ultimo_valor = pd.concat([ultimo_valor, valor_adicionado])

ultimo_valor['share_atual'] = ultimo_valor['value']/ultimo_valor['value'].sum()

preco_CPTS11 = float(input("Preço CPTS11: "))
preco_KNSC11 = float(input("Preço KNSC11: "))
preco_RBRR11 = float(input("Preço RBRR11: "))

preco_atual = pd.DataFrame({
    'Fundos Imobiliarios': ['CPTS11', 'KNSC11', 'RBRR11', 'Real'],
    'preco': [preco_CPTS11, preco_KNSC11, preco_RBRR11, 1]})

ultimo_valor = ultimo_valor.merge(preco_atual)

# Calcular o valor total do portfólio
total_portfolio_value = ultimo_valor['value'].sum()

# Calcular a quantidade alvo de cada moeda
for fi, target_share in target_balancemanto.items():
    target_value = total_portfolio_value * target_share
    current_value = ultimo_valor[ultimo_valor['Fundos Imobiliarios'] == fi]['value'].values[0]
    current_price = ultimo_valor[ultimo_valor['Fundos Imobiliarios'] == fi]['preco'].values[0]
    buy_value = target_value - current_value
    qtd_price = int(buy_value/current_price)
    if buy_value > 0:
        print(f'Comprar {qtd_price:.0f} cotas de {fi}')