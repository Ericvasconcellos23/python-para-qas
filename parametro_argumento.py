# Valores padrão e argumentos nomeados

# def verificar_status(codigo): # "codigo" é o PARÂMETRO
#     return 200 <= codigo < 300
#
# resultado = verificar_status(200) # 200 é o ARGUMENTO

# def gerar_ulr_teste(endpoint, ambiente="dev"):
#     bases = {
#         "dev": "https://dev.api.com",
#         "hml": "https://hml.api.com",
#         "prod": "https://api.com"
#     }
#
#     base = bases.get(ambiente, "https://dev.api.com")
#     return f"{base}/{endpoint}"
#
# # Sem chamar ambiente: usa "dev"
# print(gerar_ulr_teste("users"))   # https://dev.api.com/users
#
# # Passando ambiente: sobrescreve o padrão
# print(gerar_ulr_teste("users", "hml")) #  https://hml.api.com/users
# print(gerar_ulr_teste("users", "prod")) # https://api.com/users


# def criar_usuario_teste(nome, perfil="viewer", ativo=True):
#     return{"nome": nome, "perfil": perfil, "ativo": ativo}
#
# print(criar_usuario_teste("Ana QA")) # perfil=viewer, ativo=True
# print(criar_usuario_teste("Carlos", "admin")) # perfil=admin, ativo=True
# print(criar_usuario_teste("bot", "api", False)) # perfil=api, ativo=False

# Correto
# def fuc(obrigatorio, opcional="valor")
#     ...
# # Errado -> SyntaxError
# def func1(opcional="valor", obrigatorio)
#     ...

# Argumentos Nomeados

# def gerar_relatorios(suite, total, passou, falhou, ambiente="dev"):
#     taxa = (passou / total * 100) if total > 0 else 0
#     return f"[{ambiente.upper()}] {suite}: {passou}/{total} ({taxa:.0f}%)"
#
# # Posicional (pela ordem)
# print (gerar_relatorios("login", 10, 8, 2))
#
# # Nomeado (pelo nome) Código legível
# print (gerar_relatorios(suite="login", total=10, passou=8, falhou=8))

# Combinando posicionais e nomeados
# def executar_request(metodo, endpoint, timeout=30, headers=None, auth=False):
#     config = {
#         "metodo": metodo,
#         "endpoint": endpoint,
#         "timeout": timeout,
#         "headers": headers or {},
#         "auth": auth
#     }
#     return config
#
# # Obrigatórios por posição, opcipnais por nome
# executar_request("GET", "/api/users")
# executar_request("POST", "/api/users", auth=True, timeout=60)
# executar_request("GET", "/api/admin", headers={"x=Role": "admin"}, auth=True)


# ERRADO: a lista é compartilhada entre chamadas
# def adicionar_log_errado(mensagem, logs=[]):
#     logs.append(mensagem)
#     return logs
# print(adicionar_log_errado("Erro 404"))
# print(adicionar_log_errado("Erro 505")) # <- Acumulou

# # CORRETO: cada chamada cria sua própria lista
# def adicionar_log_errado(mensagem, logs=None):
#     if logs is None:
#         logs = []
#     logs.append(mensagem)
#     return logs
# print(adicionar_log_errado("Erro 404"))
# print(adicionar_log_errado("Erro 505")) # <- Independente

# Aplicação prática QA: Função de Validação Flexível
def validar_resposta_api(
        status_code,
        corpo,
        status_esperado=200,
        campos_obrigatorios=None,
        tempo_resposta=None,
        max_tempo=5.0
):
    if campos_obrigatorios is None:
        campos_obrigatorios = []
    erros = []
    if status_code != status_esperado:
        erros.append(f"Status: esperado {status_esperado}, recebeu{status_code}")
    for campo in campos_obrigatorios:
        if campo not in corpo:
            erros.append(f"Campo ausente: '{campo}' ")

    if tempo_resposta is not None and tempo_resposta > max_tempo:
        erros.append(f"Tempo: {tempo_resposta}s excedeu limite de {max_tempo}")
    print({"valido": len(erros) == 0, "erros": erros})

# Validação mínima (só status )
validar_resposta_api(200, {"id": 1})

# Com campor obrigatórios
validar_resposta_api(200, {"id": 1}, campos_obrigatorios=["id", "nome"])

# Validação completa
validar_resposta_api(
    201,
    {"id": 1},
    status_esperado=200,
    campos_obrigatorios=["id", "nome"],
    tempo_resposta=5.1
)

# Endpoint de criação (status 201)
validar_resposta_api(201, {"id": 99}, status_esperado=201)
