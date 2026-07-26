from datetime import datetime, date, time, timedelta

# Utilizando strftime - datetime para String

# dt = datetime(2024, 6, 14, 12, 5, 0)
#
# print(dt.strftime('%d/%m/%Y %H:%M:%S'))
# print(dt.strftime('%d-%m-%dT%H:%M:%SZ'))
# print(dt.strftime('%d/%m/%Y'))
# print(dt.strftime('%H:%M:%S'))
# print(dt.strftime('%Y%m%d_%H%M%S'))
# print(dt.strftime('%a, %d %b %Y %H:%M:%S'))

# Utilizando strptime - String para datetime

# Formato BR vindo de formulário

# data_str = "20/06/2024 14:32:05"
# dt = datetime.strptime(data_str, "%d/%m/%Y %H:%M:%S")
# print(dt)

# Timestampo ISO de API REST
# timestamp_api = "2024-06-20T09:15:30Z"
# dt_api = datetime.strptime(timestamp_api, "%Y-%m-%dT%H:%M:%SZ")
# print(dt_api)

# Extrair data de nome de arquivo de log
nome = "relatotio_20240620_143205.csv"
parte = nome[10:25]
dt_arquivo = datetime.strptime(parte, '%Y%m%d_%H%M%S')
print(dt_arquivo)