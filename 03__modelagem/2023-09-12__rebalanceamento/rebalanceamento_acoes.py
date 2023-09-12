import pandas as pd

data_path = ('01__carregamento_de_banco\dados_tratados\%s')

# Lendo os dados
database_acoes = pd.read_excel(
    data_path % 'Investimentos Database - PowerBI.xlsx', sheet_name='Ações')

ultima_data = database_acoes.groupby('Ações', as_index=False)['Data'].last()

ultimo_valor = database_acoes.groupby('Ações', as_index=False)['value'].last()

target_balancemanto = {
    'ABEV3': 1/17,
    'AMZO34': 1/17,
    'APPL34': 1/17,
    'BBAS3': 1/17,
    'BRKM3': 1/17,
    'COCA34': 1/17,
    'ITCL34': 1/17,
    'ITSA3': 1/17,
    'M1TA34': 1/17,
    'MGLU3': 1/17,
    'MSFT34': 1/17,
    'NVDC34': 1/17,
    'PETR4': 1/17,
    'ROXO34': 1/17,
    'TSLA34': 1/17,
    'VALE3': 1/17,
    'WEGE3': 1/17,
    'Real': 0}

valor_adicionado = pd.DataFrame({
    'Ações': ['Real'], 'value': [float(input("Aporte de Acoes: "))]})
ultimo_valor = pd.concat([ultimo_valor, valor_adicionado])

ultimo_valor['share_atual'] = ultimo_valor['value']/ultimo_valor['value'].sum()

preco_ABEV3 = float(input("Preço ABEV3: "))
preco_AMZO34 = float(input("Preço AMZO34: "))
preco_APPL34 = float(input("Preço APPL34: "))
preco_BBAS3 = float(input("Preço BBAS3: "))
preco_BRKM3 = float(input("Preço BRKM3: "))
preco_COCA34 = float(input("Preço COCA34: "))
preco_ITCL34 = float(input("Preço ITCL34: "))
preco_ITSA3 = float(input("Preço ITSA3: "))
preco_M1TA34 = float(input("Preço M1TA34: "))
preco_MGLU3 = float(input("Preço MGLU3: "))
preco_MSFT34 = float(input("Preço MSFT34: "))
preco_NVDC34 = float(input("Preço NVDC34: "))
preco_PETR4 = float(input("Preço PETR4: "))
preco_ROXO34 = float(input("Preço ROXO34: "))
preco_TSLA34 = float(input("Preço TSLA34: "))
preco_VALE3 = float(input("Preço VALE3: "))
preco_WEGE3 = float(input("Preço WEGE3: "))

preco_atual = pd.DataFrame({
    'Ações': [
        'ABEV3', 'AMZO34', 'APPL34', 'BBAS3', 'BRKM3', 'COCA34',
        'ITCL34', 'ITSA3', 'M1TA34', 'MGLU3', 'MSFT34', 'NVDC34',
        'PETR4', 'ROXO34', 'TSLA34', 'VALE3', 'WEGE3', 'Real'],
    'preco': [
        preco_ABEV3, preco_AMZO34, preco_APPL34, preco_BBAS3,
        preco_BRKM3, preco_COCA34, preco_ITCL34, preco_ITSA3,
        preco_M1TA34, preco_MGLU3, preco_MSFT34, preco_NVDC34,
        preco_PETR4, preco_ROXO34, preco_TSLA34, preco_VALE3,
        preco_WEGE3, 1]})

ultimo_valor = ultimo_valor.merge(preco_atual)

# Calcular o valor total do portfólio
total_portfolio_value = ultimo_valor['value'].sum()

# Calcular a quantidade alvo de cada moeda
for acao, target_share in target_balancemanto.items():
    target_value = total_portfolio_value * target_share
    current_value = ultimo_valor[ultimo_valor['Ações'] == acao]['value'].values[0]
    current_price = ultimo_valor[ultimo_valor['Ações'] == acao]['preco'].values[0]
    buy_value = target_value - current_value
    qtd_price = int(buy_value/current_price)
    if buy_value > 0:
        print(f'Comprar {qtd_price:.0f} cotas de {acao}')
        print(f'Equivale a R$ {qtd_price*current_price:.0f} de {acao}\n')