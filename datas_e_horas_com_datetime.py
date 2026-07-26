from datetime import datetime, date, time, timedelta

# Data atual
# hoje = date.today()
# print(hoje)
#
# # Data e hora atual
# agora = datetime.now()
# print(agora)
#
# # Criando datas fixas - essencial para dados de teste dterministicos
# data_release = date(2026, 3, 26)
# dt_deploy = datetime(2026, 3, 28, 14, 32, 0)
# print(dt_deploy)

# Dias da semana utilizando weekday()
# agora = datetime(2026, 7, 26, 11, 10, 5)
#
# dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
# print(agora.weekday())
# print(dias_semana[agora.weekday()])
#
#
# # Verificar se um evento ocorreu em dia útil
# def e_dia_util(dt):
#     return dt.weekday() < 5
#
# print(e_dia_util(agora))

# Timedelta - Representando Duração

# uma_semana = timedelta(weeks=1)
# dois_dias = timedelta(days=2)
# duas_horas = timedelta(hours=2)
# trinta_min = timedelta(minutes=30)
#
# print(uma_semana)
# print(dois_dias)
# print(duas_horas)
# print(trinta_min)

# Adição e Subtração de dias

# hoje = date(2026, 7, 26)
# print(hoje + timedelta(days=7))
# print(hoje - timedelta(days=30))

# Exemplo real: expiração de token

# data_criacao = datetime(2026, 7, 26, 10, 0, 0)
# validade = timedelta(hours=24)
# data_expiracao = data_criacao + validade
#
# momento_acesso = datetime(2026, 7, 27, 11, 0, 0)
# print(f"{momento_acesso > data_expiracao} Token expirado !")

# Diferença entre Datas
# .seconds() não inclui os dias. Para durações que podem ultrapassar 24h, sempre use .total_seconds()

# inicio_teste = datetime(2024, 6, 20, 9, 0, 0)
# fim_teste = datetime(2024, 6, 20, 11, 37, 45)
#
# duracao = fim_teste - inicio_teste
#
# print(duracao)
# print(duracao.days)
# print(duracao.seconds)
# print(duracao.total_seconds())

# Aplicação Prática - Cenáriios de QA
# Cenário 1: Validade de sessão de usuário

# login_em = datetime(2024, 6, 20, 8, 0)
# timeout_sessao = timedelta(minutes=30)
# expira_em = login_em + timeout_sessao
#
# tentativa_acesso = datetime(2024, 6, 20, 8, 45, 0)
# sessao_valida = tentativa_acesso <= expira_em
# print(sessao_valida)

# Cenário 2: Tempo Total de execução de suítes de testes

execucoes = [
    ("Login", datetime(2024,6,20,9,0,0),
     datetime(2024,6,20,9,0,0)),

    ("Cadastro", datetime(2024,6,20,9,0,2),
     datetime(2024,6,20,9,0,8)),

    ("Busca produto", datetime(2024,6,20,9,0,8),
     datetime(2024,6,20,9,0,9)),

    ("Checkout", datetime(2024,6,20,9,0,9),
     datetime(2024,6,20,9,0,25)),
]

total = timedelta()
for nome, ini, fim in execucoes:
    dur = fim - ini
    total += dur
    print(f"{nome:<20} {dur.seconds}s")

print(f"Total: {total}s")