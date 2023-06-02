from datetime import datetime

datafmt = '%d/%m/%Y'

data = datetime.strptime('2022-4-20', '%Y-%m-%d')# so acresentar horas e minutos como quiser

print(data.strftime(datafmt))

## Ajustando as DATAS