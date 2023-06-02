from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_empretimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_empretimo + delta_anos

data_parcelas = []
data_parcela = data_empretimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)


numero_parcelas = len(data_parcelas)
valor_parce = valor_total / numero_parcelas

for data in data_parcelas:
    print( f"Data da parcela: {data.strftime('%d/%m/%Y')}\
           Valor da parcela: R${valor_parce:,.2f}")

