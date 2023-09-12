import numpy as np
import pandas as pd

data_path = ('01__carregamento_de_banco\dados_tratados\%s')

# Lendo os dados
database_fi = pd.read_excel(
    data_path % 'Investimentos Database - PowerBI.xlsx', sheet_name='Fundos Imobiliários')
database_fi.rename({'Fundos Imobiliarios': 'ativo'}, axis=1, inplace=True)

database_criptomoedas = pd.read_excel(
    data_path % 'Investimentos Database - PowerBI.xlsx', sheet_name='Criptomoedas')
database_criptomoedas.rename({'Criptomoedas': 'ativo'}, axis=1, inplace=True)

database_acoes = pd.read_excel(
    data_path % 'Investimentos Database - PowerBI.xlsx', sheet_name='Ações')
database_acoes.rename({'Ações': 'ativo'}, axis=1, inplace=True)

database = pd.concat([database_fi, database_criptomoedas, database_acoes])

ultima_data = database.groupby('ativo', as_index=False)['Data'].last()

ultimo_valor = database.groupby('ativo', as_index=False)['value'].last()
ultimo_valor = ultimo_valor.copy()[ultimo_valor['ativo']!='Ethereum POW']

target_balancemanto = {
    'CPTS11': 0.5 * 1/3,
    'KNSC11': 0.5 * 1/3,
    'RBRR11': 0.5 * 1/3,
    'ABEV3': 0.3 * 1/17,
    'AMZO34': 0.3 * 1/17,
    'APPL34': 0.3 * 1/17,
    'BBAS3': 0.3 * 1/17,
    'BRKM3': 0.3 * 1/17,
    'COCA34': 0.3 * 1/17,
    'ITCL34': 0.3 * 1/17,
    'ITSA3': 0.3 * 1/17,
    'M1TA34': 0.3 * 1/17,
    'MGLU3': 0.3 * 1/17,
    'MSFT34': 0.3 * 1/17,
    'NVDC34': 0.3 * 1/17,
    'PETR4': 0.3 * 1/17,
    'ROXO34': 0.3 * 1/17,
    'TSLA34': 0.3 * 1/17,
    'VALE3': 0.3 * 1/17,
    'WEGE3': 0.3 * 1/17,
    'Bitcoin': 0.2 * 1/2,
    'Ethereum': 0.2 * 1/4,
    'Cardano': 0.2 * 1/12,
    'EOS': 0.2 * 1/12,
    'Litecoin': 0.2 * 1/12,
    'Real': 0}

aporte_adicional = float(input("Aporte mensal (R$): "))
valor_adicionado = pd.DataFrame({
    'ativo': ['Real'], 'value': [aporte_adicional]})
ultimo_valor = pd.concat([ultimo_valor, valor_adicionado])

ultimo_valor['share_atual'] = ultimo_valor['value']/ultimo_valor['value'].sum()

preco_CPTS11 = float(input("Preço CPTS11: "))
preco_KNSC11 = float(input("Preço KNSC11: "))
preco_RBRR11 = float(input("Preço RBRR11: "))

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

preco_acoes = pd.DataFrame({
    'ativo': [
        'ABEV3', 'AMZO34', 'APPL34', 'BBAS3', 'BRKM3', 'COCA34',
        'ITCL34', 'ITSA3', 'M1TA34', 'MGLU3', 'MSFT34', 'NVDC34',
        'PETR4', 'ROXO34', 'TSLA34', 'VALE3', 'WEGE3'],
    'preco': [
        preco_ABEV3, preco_AMZO34, preco_APPL34, preco_BBAS3,
        preco_BRKM3, preco_COCA34, preco_ITCL34, preco_ITSA3,
        preco_M1TA34, preco_MGLU3, preco_MSFT34, preco_NVDC34,
        preco_PETR4, preco_ROXO34, preco_TSLA34, preco_VALE3,
        preco_WEGE3]})

preco_fi = pd.DataFrame({
    'ativo': ['CPTS11', 'KNSC11', 'RBRR11', 'Real'],
    'preco': [preco_CPTS11, preco_KNSC11, preco_RBRR11, 1]})

preco_atual = pd.concat([preco_acoes, preco_fi])

ultimo_valor = ultimo_valor.merge(preco_atual, how='left')

# Calcular o valor total do portfólio
total_portfolio_value = ultimo_valor['value'].sum()

# Inicializar um dicionário para rastrear as compras
ativos_comprar = []
valores_comprar = []
qtd_comprar = []
preco_comprar = []

# Calcular a quantidade alvo de cada moeda
for ativo, target_share in target_balancemanto.items():
    target_value = total_portfolio_value * target_share
    current_value = ultimo_valor[ultimo_valor['ativo'] == ativo]['value'].values[0]
    current_price = ultimo_valor[ultimo_valor['ativo'] == ativo]['preco'].values[0]
    if np.isnan(current_price):
        current_price = 1
    buy_value = target_value - current_value
    qtd_price = int(buy_value/current_price)
    if qtd_price*current_price > 0:
        ativos_comprar.append(ativo)
        valores_comprar.append(qtd_price*current_price)
        qtd_comprar.append(qtd_price)
        preco_comprar.append(current_price)

compras = pd.DataFrame({
    'ativos': ativos_comprar,
    'valor': valores_comprar,
    'qtd': qtd_comprar,
    'preco': preco_comprar})

# Verificar se a soma das compras ultrapassa o aporte adicional
soma_compras = sum(compras['valor'])
if soma_compras > aporte_adicional:
    fator_reducao = aporte_adicional / soma_compras
    compras['fator_reducao'] = fator_reducao

compras['valor'] = compras['valor'] * compras['fator_reducao']
compras['qtd'] = (compras['valor'] / compras['preco']).astype(int)

print("Compras a serem executadas")
print(compras)