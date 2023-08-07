import pandas as pd

data_path_1 = ('01__carregamento_de_banco\dados_brutos\%s')
data_path_2 = ('01__carregamento_de_banco\dados_tratados\%s')

# Lendo os dados
database_criptomoedas = pd.read_excel(
    data_path_1 % 'Investimentos - Base de Dados.xlsx', sheet_name='Criptomoedas')

database_acoes = pd.read_excel(
    data_path_1 % 'Investimentos - Base de Dados.xlsx', sheet_name='Ações')

database_fi = pd.read_excel(
    data_path_1 % 'Investimentos - Base de Dados.xlsx', sheet_name='Fundos Imobiliários')

database_div_acoes = pd.read_excel(
    data_path_1 % 'Investimentos - Base de Dados.xlsx', sheet_name='Ações_Dividendos-Juros')

database_div_fi = pd.read_excel(
    data_path_1 % 'Investimentos - Base de Dados.xlsx', sheet_name='Fundos Imobiliários_Dividendos')

database_caixinhas = pd.read_excel(
    data_path_1 % 'Investimentos - Base de Dados.xlsx', sheet_name='Caixinhas Nubank')

database_de_para = pd.read_excel(
    data_path_1 % 'Investimentos - Base de Dados.xlsx', sheet_name='De-Para')

# Tratando Criptomoedas
database_criptomoedas = pd.melt(database_criptomoedas, id_vars='Data')
database_criptomoedas.rename({'variable': 'Criptomoedas'}, axis=1, inplace=True)

# Tratando FI
database_fi = pd.melt(database_fi, id_vars='Data')
database_fi.rename({'variable': 'Fundos Imobiliarios'}, axis=1, inplace=True)

# Tratando Acoes
database_acoes = pd.melt(database_acoes, id_vars='Data')
database_acoes.rename({'variable': 'Ações'}, axis=1, inplace=True)

# Tratando Dividendos Acoes
database_div_acoes = pd.melt(database_div_acoes, id_vars='Data')
database_div_acoes.rename({'variable': 'Ações'}, axis=1, inplace=True)

# Tratando Dividendos FI
database_div_fi = pd.melt(database_div_fi, id_vars='Data')
database_div_fi.rename({'variable': 'Fundos Imobiliarios'}, axis=1, inplace=True)

# Tratando Caixinhas
database_caixinhas = pd.melt(database_caixinhas, id_vars='Data')
database_caixinhas.rename({'variable': 'Caixinhas'}, axis=1, inplace=True)

# Salvando dados
writer = pd.ExcelWriter(data_path_2 % 'Investimentos Database - PowerBI.xlsx', engine='xlsxwriter')

# salvar cada DataFrame em uma aba separada
database_criptomoedas.to_excel(writer, sheet_name='Criptomoedas', index=False)
database_acoes.to_excel(writer, sheet_name='Ações', index=False)
database_fi.to_excel(writer, sheet_name='Fundos Imobiliários', index=False)
database_div_acoes.to_excel(writer, sheet_name='Ações_Dividendos-Juros', index=False)
database_div_fi.to_excel(writer, sheet_name='Fundos Imobiliários_Dividendos', index=False)
database_caixinhas.to_excel(writer, sheet_name='Caixinhas Nubank', index=False)
database_de_para.to_excel(writer, sheet_name='De-Para', index=False)

# salvar o arquivo Excel
writer.close()