# Args: Argumentos posicisionais variaveis
# Temos uma tupla com args
# def logar_resultado(teste, *detalhes):
#     print(f"[LOG] teste: {teste}")
#     for detalhe in detalhes:
#         print(f"- {detalhe}")
#
#
# logar_resultado ("login", "status: 200", "tempo: 1.2")
#
# logar_resultado ("Cadastro", "status: 201", "tempo: 0.8", "usuario criado", "email enviado")
#
# logar_resultado ("Health Check")

# Exemplo no ambiente de QA
# def todos_sucessos(*status_codes):
#     for code in status_codes:
#         if not (200 <= code < 300):
#             return False
#     return True
#
# print(todos_sucessos(200, 201, 204)) # True
# todos_sucessos(200, 404, 201) # False (404 não é sucesso)
# todos_sucessos() # True (nanhum falhou)


# Kwargs: Argumentos Nomeados Variaveis
# Temos um dicionário com kwargs

# def configurar_requisicao(url, **opcoes):
#     print(f" URL: {url}")
#     for chave, valor in opcoes.items():
#         print(f" {chave}: {valor}")
#
# configurar_requisicao(
#     "https://api.exemplo.com/users",
#     metodo="GET",
#     timeout=30,
#     verificar_ssl=True
# )

# Usando Args e Kwargs juntos para isso existe uma regra
# Primeiro os parâmetros normais, depois args e por último kwargs
# def executar_teste(nome_teste, *passos, **config):
#     print(f"Teste: {nome_teste}")
#     for i, passo in enumerate(passos, 1):
#         print(f" {i}. {passo}")
#
#     for chave, valor in config.items():
#         print(f"{chave}: {valor}")
#
# executar_teste(
#     "Fluxo de compra", # nome_teste (Normal)
#     "Acesso catalogo",   # *passos
#     "Adicionar ao carrinho",     # *passos
#     "Finalizar pedido",          # *passos
#     ambientes="producao",        # **config
#     navegador="Chrome"           # **config
# )

# Aplicação Prática QA: Funcao de Log Flexivel
from datetime import datetime

def registrar_evento(nivel, mensagem, *tags, **contexto):
    timestamp = datetime.now() .strftime('%d/%m/%Y %H:%M:%S')
    linha = f"[{timestamp}] [{nivel.upper()}] {mensagem}"
    if tags:
        linha += f" | tags: {', '.join(tags)}"
    print(linha)
    for chave, valor in contexto.items():
        print(f"  {chave}: {valor}")


# Simples
# registrar_evento("info", "Teste iniciado")

# Com tags
# registrar_evento("warn", "resposta lenta", "Performance", "api")

# # Com tags e Texto
# registrar_evento("erro", "Falha na autenticação", "auth",
#                  endpoint="/api/login", status_code=400, tentativa=3)
# # Reutilizando contexto
contexto_ci = {"pipeline": "CI-1234", "branch": "main" }
registrar_evento("info", "Deploy realizado", "deploy", **contexto_ci)